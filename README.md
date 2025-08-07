# 🧠 MedXAI - Medical Report Interpreter

MedXAI is a medical assistant that lets you upload long medical reports (like blood tests, CSRs, X-rays converted to text, etc.), extracts their content, retrieves relevant sections, and generates clinically grounded interpretations using LLMs.

It uses **Retrieval-Augmented Generation (RAG)** to handle reports that exceed LLM context limits, ensuring your questions are answered accurately based on your specific report content.

---

## 🚀 Features

✅ Upload medical reports as PDFs  
✅ Automatically extract and preview report text  
✅ Smart text chunking for long documents  
✅ Vector-based retrieval (FAISS) for relevant report sections  
✅ Natural language Q&A with GPT-4  
✅ Secure and it works locally, your data isn’t stored elsewhere

---

## 📂 Folder Structure
MedXAI/
├── app.py                         # Main Streamlit app entrypoint
├── .env                           # Stores your OpenAI API key
├── requirements.txt               # All Python dependencies
├── README.md                      # Project documentation

├── prompts/
│   └── interpretation.txt         # System prompt to guide GPT medical behavior

├── utils/
│   ├── pdf_parser.py              # Extracts text from uploaded PDF reports
│   ├── splitter.py                # Splits long reports into manageable text chunks
│   ├── vector_store.py            # Embeds chunks and retrieves relevant ones using FAISS
│   └── qa_engine.py               # Sends user queries + context to GPT-4 for interpretation


---

## 🔧 Setup

1️⃣ Clone the repo:
```bash
git clone https://github.com/sreyasxkumar/MedXAI.git
cd MedXAI
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Add your OpenAI API key in .env file:
```bash
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXX
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```
Then open the Streamlit URL shown in your terminal (typically http://localhost:8501).

---

## 📝 How to Use

- Upload your medical report (PDF) → The app will extract and split the text.
- Preview extracted report text → See what was parsed from the PDF.
- Ask a question → e.g., "What does the blood test reportindicate?"
- The app retrieves relevant parts of your report and generates a clinically relevant answer using LLMs.

---

## 📦 Requirements
- streamlit
- openai>=1.0.0
- python-dotenv
- PyMuPDF
- langchain
- faiss-cpu

```bash
pip install -r requirements.txt
```

---

## 🔒 Data Privacy
Your report is processed locally on your machine. Only the relevant text chunks and your question are sent to OpenAI’s API for interpretation.

---



