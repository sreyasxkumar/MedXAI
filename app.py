import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.splitter import split_medical_report
from utils.vector_store import create_vector_store, retrieve_relevant_chunks
from utils.qa_engine import generate_answer
import os

st.set_page_config(page_title="MedXAI - Clinical Interpreter", layout="wide")
st.title("🧠 MedXAI - Medical Report Interpreter")

# Session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "chunks" not in st.session_state:
    st.session_state.chunks = None
if "text" not in st.session_state:
    st.session_state.text = ""

# Upload section
uploaded_file = st.file_uploader("📄 Upload your blood test or medical report (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting and processing your report..."):
        raw_text = extract_text_from_pdf(uploaded_file)
        st.session_state.text = raw_text

        chunks = split_medical_report(raw_text)
        st.session_state.chunks = chunks

        vector_store = create_vector_store(chunks)
        st.session_state.vector_store = vector_store

    st.success("✅ Report processed successfully!")

    st.subheader("📝 Extracted Report Preview")
    st.text_area("Report Text", value=st.session_state.text, height=300)

    st.subheader("💬 Ask a Clinical Question")
    user_query = st.text_input("Example: 'Is there any vitamin deficiency?' or 'What does my lipid profile suggest?'")

    if user_query and st.button("🔍 Interpret"):
        with st.spinner("🔬 Generating interpretation..."):
            top_chunks = retrieve_relevant_chunks(user_query, st.session_state.vector_store)
            answer = generate_answer(user_query, top_chunks)
            st.subheader("📊 AI Interpretation")
            st.markdown(answer)
