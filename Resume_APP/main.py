from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tempfile

app = Flask(__name__)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    scores = cosine_similarity([job_vector], resume_vectors).flatten()
    return scores.tolist()

@app.route("/", methods=["POST"])
def resume_ranking():
    job_description = request.form.get("job_description")
    files = request.files.getlist("resumes")

    if not job_description or not files:
        return jsonify({"error": "Missing job description or resumes"}), 400

    resumes_text = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file.save(temp.name)
            resumes_text.append(extract_text_from_pdf(temp.name))

    scores = rank_resumes(job_description, resumes_text)
    names = [file.filename for file in files]
    return jsonify(dict(zip(names, scores)))
