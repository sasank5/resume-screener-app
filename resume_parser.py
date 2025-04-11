import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Test it (for now)
if __name__ == "_main_":
    resume_path = "sample_resumepdf"  # Add a resume file to your folder
    text = extract_text_from_pdf(resume_path)
    print("Extracted Resume Text:\n")
    print(text[:1000])  # Print first 1000 characters