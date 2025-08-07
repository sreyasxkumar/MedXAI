from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_medical_report(text, chunk_size=700, chunk_overlap=100):
    """
    Splits large medical reports into overlapping text chunks for embedding.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splitter.split_text(text)
    return chunks
