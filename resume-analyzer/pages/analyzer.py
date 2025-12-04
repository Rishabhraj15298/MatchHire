import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import PyPDF2 as pdf
import re

# Load environment variables and configure API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Page config
st.set_page_config(
    page_title="Resume Analyzer - MatchHire",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.page_link("home.py", label="⬅️ Back to Home")
# Helper functions
def get_response(prompt, text, jd):
    """Generate response from Gemini with prompt + resume + JD"""
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt.format(resume=text, job_desc=jd))
    return response.text

def input_pdf_text(file):
    """Extract text from PDF"""
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Review the following resume against the provided job description. 
Highlight strengths and weaknesses of the candidate in relation to the role.

Job Description:
{job_desc}

Resume:
{resume}
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System) with expertise in resume screening. 
Evaluate the resume against the provided job description.

Tasks:
1. Provide a percentage match score (just a number between 0-100).
2. List missing important keywords.
3. Give final thoughts about the overall suitability.

Job Description:
{job_desc}

Resume:
{resume}
"""

# Analyzer UI
def show_analyzer():
    # Custom CSS for dark mode
    st.markdown(
        """
        <style>
        .stApp { background-color: #0a0a0a; color: #e4e4e7; }
        h1, h2, h3, h4, h5, h6, p, label { color: white !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("AI Resume Analyzer")

    # Inputs
    jd = st.text_area("Paste the Job Description", height=250)
    uploaded_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

    if uploaded_file is not None:
        st.success("✅ PDF Uploaded Successfully")

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        submit1 = st.button("Tell Me About the Resume")
    with col2:
        submit3 = st.button("Percentage Match (ATS)")

    # Actions
    if submit1:
        if uploaded_file is not None and jd:
            with st.spinner("Analyzing resume..."):
                pdf_content = input_pdf_text(uploaded_file)
                response = get_response(input_prompt1, pdf_content, jd)
                st.subheader("Recruiter-Style Evaluation")
                st.write(response)
        else:
            st.error("Please upload a resume and paste the job description.")

    elif submit3:
        if uploaded_file is not None and jd:
            with st.spinner("Running ATS scan..."):
                pdf_content = input_pdf_text(uploaded_file)
                response = get_response(input_prompt3, pdf_content, jd)

                # Try extracting a percentage score from the response
                match = re.search(r"(\d{1,3})%", response)
                if match:
                    score = int(match.group(1))
                    st.metric("ATS Match Score", f"{score}%")
                else:
                    st.metric("ATS Match Score", "N/A")

                st.subheader("Detailed ATS Feedback")
                st.write(response)
        else:
            st.error("Please upload a resume and paste the job description.")

    # --- Back to Home Button ---
    st.divider()
    

# Main
def main():
    show_analyzer()

if __name__ == "__main__":
    main()
