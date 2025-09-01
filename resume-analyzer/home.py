import streamlit as st

# Page config
st.set_page_config(
    page_title="MatchHire - AI Resume Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional dark theme
st.markdown(
    """
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Dark background and typography */
        .stApp {
            background: linear-gradient(135deg, #0a0f1c 0%, #1a1f2e 100%);
            color: white;
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide sidebar completely */
        [data-testid="stSidebar"] {
            display: none;
        }
        
        /* Hero container */
        .hero-container {
            text-align: center;
            padding: 100px 20px 80px 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Logo/Brand styling */
        .brand-logo {
            font-size: 48px;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 16px;
            letter-spacing: -1px;
        }
        
        /* Tagline */
        .tagline {
            font-size: 20px;
            color: #a0aec0;
            margin-bottom: 12px;
            font-weight: 400;
        }
        
        /* Description */
        .description {
            font-size: 16px;
            color: #718096;
            margin-bottom: 50px;
            line-height: 1.6;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        /* Features grid */
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 24px;
            margin: 60px 0;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-2px);
            border-color: rgba(102, 126, 234, 0.3);
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.1);
        }
        
        .feature-icon {
            font-size: 32px;
            margin-bottom: 16px;
        }
        
        .feature-title {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #e2e8f0;
        }
        
        .feature-text {
            font-size: 14px;
            color: #a0aec0;
            line-height: 1.5;
        }
        
        /* Button styling */
        .stButton button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 16px 32px;
            font-size: 16px;
            font-weight: 600;
            font-family: 'Inter', sans-serif;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
            min-width: 200px;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(102, 126, 234, 0.4);
            background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
        }
        
        .stButton button:active {
            transform: translateY(0px);
        }
        
        /* Stats section */
        .stats-container {
            background: rgba(255, 255, 255, 0.03);
            border-radius: 16px;
            padding: 40px;
            margin: 60px 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 32px;
            text-align: center;
        }
        
        .stat-number {
            font-size: 36px;
            font-weight: 700;
            color: #667eea;
            margin-bottom: 8px;
        }
        
        .stat-label {
            font-size: 14px;
            color: #a0aec0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .brand-logo {
                font-size: 36px;
            }
            .tagline {
                font-size: 18px;
            }
            .description {
                font-size: 15px;
            }
            .hero-container {
                padding: 60px 20px 40px 20px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Hero Section
st.markdown(
    """
    <div class="hero-container">
        <div class="brand-logo">MatchHire</div>
        <div class="tagline">AI-Powered Resume Intelligence</div>
        <div class="description">
            Transform your job search with advanced ATS optimization, keyword analysis, 
            and personalized recommendations powered by artificial intelligence.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Features Section
st.markdown(
    """
    <div class="features-grid">
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">ATS Optimization</div>
            <div class="feature-text">
                Ensure your resume passes through Applicant Tracking Systems 
                with our advanced compatibility analysis.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Keyword Analysis</div>
            <div class="feature-text">
                Get detailed insights on missing keywords and industry-specific 
                terms to boost your visibility.
            </div>
        </div>
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">Instant Results</div>
            <div class="feature-text">
                Receive comprehensive feedback and actionable recommendations 
                in seconds, not hours.
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Stats Section
st.markdown(
    """
    <div class="stats-container">
        <div class="stats-grid">
            <div>
                <div class="stat-number">98%</div>
                <div class="stat-label">ATS Compatibility</div>
            </div>
            <div>
                <div class="stat-number">50K+</div>
                <div class="stat-label">Resumes Analyzed</div>
            </div>
            <div>
                <div class="stat-number">3x</div>
                <div class="stat-label">Higher Interview Rate</div>
            </div>
            <div>
                <div class="stat-number">24/7</div>
                <div class="stat-label">Available</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Call-to-action button (centered)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Analyze Your Resume", use_container_width=True):
        st.switch_page("pages/analyzer.py")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 80px; padding: 40px 20px; border-top: 1px solid rgba(255, 255, 255, 0.1);">
        <p style="color: #718096; font-size: 14px; margin: 0;">
            Powered by advanced AI technology • Secure & confidential • GDPR compliant
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)