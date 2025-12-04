import streamlit as st
import requests
import os
from dotenv import load_dotenv
import PyPDF2 as pdf
import re
import json

# Load .env (local) — Streamlit Cloud will use st.secrets
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets["api_keys"]["gemini_api_key"]
MODEL = "gemini-2.0-flash"
    
# Streamlit Page Config
st.set_page_config(
    page_title="Resume Analyzer - MatchHire",
    page_icon="📃",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.page_link("home.py", label="⬅️ Back to Home")

# ------------------------ GEMINI REST API CALL ------------------------
def gemini_generate(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "❌ Error: No response generated from the AI."

# ------------------------ PDF TEXT EXTRACTOR ------------------------
def input_pdf_text(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# ------------------------ PROMPTS ------------------------
input_prompt1 = """
You are an experienced Technical HR Manager.
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

# ------------------------ MAIN UI ------------------------
def show_analyzer():

    # Dark Theme
    st.markdown("""
        <style>
        .stApp { background-color: #0a0a0a; color: #e4e4e7; }
        h1, h2, h3, h4, h5, h6, p, label { color: white !important; }
        </style>
    """, unsafe_allow_html=True)

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

    # ---- Recruiter Style Review ----
    if submit1:
        if uploaded_file and jd:
            with st.spinner("Analyzing resume..."):
                pdf_content = input_pdf_text(uploaded_file)
                prompt = input_prompt1.format(resume=pdf_content, job_desc=jd)
                response = gemini_generate(prompt)

                st.subheader("Recruiter-Style Evaluation")
                st.write(response)
        else:
            st.error("Please upload a resume and paste the job description.")

    # ---- ATS MODE ----
    if submit3:
        if uploaded_file and jd:
            with st.spinner("Running ATS scan..."):
                pdf_content = input_pdf_text(uploaded_file)
                prompt = input_prompt3.format(resume=pdf_content, job_desc=jd)
                response = gemini_generate(prompt)

                # Extract score using regex
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

    st.divider()


def main():
    show_analyzer()


if __name__ == "__main__":
    main()
