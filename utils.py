from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
import streamlit as st


# List of credits  based on pdf
credit_words = [
    "Sustainable Architecture and Design",
    "Site Selection and Planning",
    "Water Conservation",
    "Energy Efficiency",
    "Building Materials and Resources",
    "Indoor Environmental Quality",
    "Innovation and Development"
]

@st.cache_resource #load the vector db only once

def load_and_index_pdf(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load_and_split()

    # Assign credits to pages
    for page in pages:
        assigned_credit = "General"
        last_words = page.page_content.split()[-4:]
        last_words_string = " ".join(last_words)
        for credit_word in credit_words:
            if credit_word.lower() in last_words_string.lower():
                assigned_credit = credit_word
                break
        page.metadata["credit"] = assigned_credit

    # Split pages into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=200,
    )
    chunked_documents = text_splitter.split_documents(pages)

    # Create embeddings and vector store
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunked_documents, embeddings)
    return vectorstore

# Retrieve top 2 chunks
def retrieve_relevant_chunks(vectorstore, query: str, credit: str = None, top_k: int = 2):
    if credit == "All" or credit is None: 
        retrieved_chunks = vectorstore.similarity_search(query, k=top_k)
    else:
        retrieved_chunks = vectorstore.similarity_search(query, k=top_k, filter={"credit": credit})
    return retrieved_chunks