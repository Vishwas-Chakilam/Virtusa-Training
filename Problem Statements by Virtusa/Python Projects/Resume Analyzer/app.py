import streamlit as st
import nlp_utils
import matplotlib.pyplot as plt
import pandas as pd
import io

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #0d6efd;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0b5ed7;
        box-shadow: 0 4px 12px rgba(13, 110, 253, 0.3);
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border: 1px solid #e9ecef;
        text-align: center;
    }
    .skill-tag {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 16px;
        font-size: 0.85em;
        margin: 4px;
        font-weight: 500;
    }
    .match-tag { background-color: #d1e7dd; color: #0f5132; }
    .miss-tag { background-color: #fff3cd; color: #664d03; }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("Resume Analyzer")
    st.markdown("---")

    with st.sidebar:
        st.header("About")
        st.info("This tool uses NLP to compare your resume against a job description and provides a skill match score and gap analysis.")
        st.markdown("### How to use:")
        st.write("1. Paste the Job Description.")
        st.write("2. Upload your Resume (PDF).")
        st.write("3. Hit 'Analyze Match'.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Job Description")
        jd_text = st.text_area("Paste the JD here...", height=250, placeholder="Required skills, responsibilities...")

    with col2:
        st.subheader("👤 Applicant Profile")
        uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
        
        resume_text = ""
        if uploaded_file is not None:
            # We need to save the uploaded file temporarily or handle it as a stream
            # nlp_utils.get_pdf_text_util expects a path.
            # Let's modify nlp_utils or handle it here.
            # In Streamlit, uploaded_file is a file-like object.
            
            try:
                import PyPDF2
                pdf = PyPDF2.PdfReader(uploaded_file)
                resume_text = "".join([p.extract_text() or "" for p in pdf.pages])
                st.success("Resume loaded successfully!")
            except Exception as e:
                st.error(f"Error reading PDF: {e}")
        
        manual_resume = st.text_area("Or paste Resume text here...", height=100, placeholder="Paste text if not uploading PDF...")
        if manual_resume:
            resume_text = manual_resume

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("GENERATE MATCH SCORE"):
        if not jd_text or not resume_text:
            st.warning("Please provide both a Job Description and a Resume.")
        else:
            with st.spinner("Analyzing skill semantic match..."):
                # Extraction
                jd_skills = nlp_utils.extract_meaningful_tech_skills(jd_text)
                res_skills = nlp_utils.extract_meaningful_tech_skills(resume_text)
                
                matches = jd_skills.intersection(res_skills)
                missing = jd_skills.difference(res_skills)
                
                if not jd_skills:
                    st.error("No meaningful technical keywords could be identified in the JD.")
                    return

                score = (len(matches) / len(jd_skills)) * 100

                # Results Display
                st.markdown("---")
                
                m1, m2, m3 = st.columns(3)
                with m1:
                    st.markdown(f'<div class="metric-card"><h3>Match Score</h3><h1 style="color:#0d6efd;">{round(score, 1)}%</h1></div>', unsafe_allow_html=True)
                with m2:
                    st.markdown(f'<div class="metric-card"><h3>Matches</h3><h1 style="color:#198754;">{len(matches)}</h1></div>', unsafe_allow_html=True)
                with m3:
                    st.markdown(f'<div class="metric-card"><h3>Gaps</h3><h1 style="color:#f39c12;">{len(missing)}</h1></div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                res_col1, res_col2 = st.columns([2, 1])

                with res_col1:
                    st.subheader("🔍 Detailed Analysis")
                    
                    st.write("**✔ Technical Matches**")
                    if matches:
                        match_html = "".join([f'<span class="skill-tag match-tag">{s}</span>' for s in sorted(list(matches))])
                        st.markdown(match_html, unsafe_allow_html=True)
                    else:
                        st.write("_No direct technical matches found._")

                    st.write("<br>**🚫 Targeted Skills for Improvement**", unsafe_allow_html=True)
                    if missing:
                        miss_html = "".join([f'<span class="skill-tag miss-tag">{s}</span>' for s in sorted(list(missing))])
                        st.markdown(miss_html, unsafe_allow_html=True)
                    else:
                        st.write("_Your resume matches all identified JD skills!_")

                with res_col2:
                    st.subheader("📊 Skills Gap")
                    
                    fig, ax = plt.subplots(figsize=(5, 4))
                    labels = ['Matches', 'Gaps']
                    values = [len(matches), len(missing)]
                    colors = ['#198754', '#f39c12']
                    
                    bars = ax.bar(labels, values, color=colors, width=0.6)
                    ax.set_title("Core Skills Analysis", fontsize=12, fontweight='bold', pad=20)
                    ax.spines['top'].set_visible(False)
                    ax.spines['right'].set_visible(False)
                    
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                                f'{int(height)}', ha='center', va='bottom', fontweight='bold')
                    
                    st.pyplot(fig)

if __name__ == "__main__":
    main()
