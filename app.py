import streamlit as st
from resume_parser import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile

st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("AI Resume Matcher")
st.markdown("Upload your resume and paste a job description to see the match score.")

# Upload resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Paste Job Description")

# Match button
if resume_file and job_description:
    if st.button("Check Match Score"):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(resume_file.read())
            temp_path = tmp_file.name
        
        # Extract resume text
        resume_text = extract_text_from_pdf(temp_path)

        # Compute similarity
        docs = [resume_text, job_description]
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(docs)
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

        st.success(f"Match Score: {score:.2f}%")