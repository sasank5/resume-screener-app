from resume_parser import extract_text_from_pdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_resume_with_job(resume_text, job_desc):
    documents = [resume_text, job_desc]
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity_score * 100

# Load resume
resume_text = extract_text_from_pdf("sample_resume.pdf")

# Sample Job Description
job_description = """
We are looking for a Python Developer with experience in machine learning, data preprocessing,
and cloud tools like Docker or AWS. The candidate should have a strong foundation in statistics,
data structures, and model evaluation techniques.
"""

# Compare
score = match_resume_with_job(resume_text, job_description)
print(f"\nMatch Score: {score:.2f}%")