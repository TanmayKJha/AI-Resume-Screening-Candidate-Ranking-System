# 🧠 AI Resume Screening & Candidate Ranking System

A smart, AI-powered resume screening tool built using **Streamlit** that automates the process of matching resumes to job descriptions and ranks candidates based on relevance.

---

## 🚀 Features

- 📄 Upload multiple resumes (PDF) at once — up to **200MB total**
- 📝 Input custom job descriptions
- 🤖 Uses **TF-IDF vectorization** and **cosine similarity** to compute relevance
- 📊 Displays a **ranked table** of resumes with matching scores
- ⚡ Fast and lightweight with a simple **Streamlit** interface

---

## 🧠 How It Works

1. **Job Description Input**: Enter the desired job description in the provided text area.
2. **Resume Upload**: Upload one or more resume files in PDF format.
3. **Text Extraction**: The app extracts and processes resume text using PyPDF2.
4. **Similarity Scoring**: All resumes are compared to the job description using TF-IDF and cosine similarity.
5. **Ranking**: Resumes are ranked based on similarity scores, helping identify the best-matching candidates quickly.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** — for the interactive web UI
- **PyPDF2** — to extract text from PDF resumes
- **scikit-learn** — for TF-IDF vectorization & cosine similarity
- **pandas** — for tabular output

---

## 📸 Screenshot

![screenshot](https://github.com/TanmayKJha/AI-Resume-Screening-Candidate-Ranking-System/blob/main/HomePage.png)
![screenshot](https://github.com/TanmayKJha/AI-Resume-Screening-Candidate-Ranking-System/blob/main/Output.png)
![screenshot](https://github.com/TanmayKJha/AI-Resume-Screening-Candidate-Ranking-System/blob/main/RankingOutput.png)

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/TanmayKJha/AI-Resume-Screening-Candidate-Ranking-System.git
cd AI-Resume-Screening-Candidate-Ranking-System
