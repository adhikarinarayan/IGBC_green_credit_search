import streamlit as st
from utils import credit_words ,load_and_index_pdf, retrieve_relevant_chunks

# Load the PDF and create the vectorstore

pdf_path = "file\IGBC_Green_New_Buildings_Rating_System_(Version_3.0_with_Fifth_Addendum).pdf"  #  PDF path
vectorstore = load_and_index_pdf(pdf_path)

#===============================================================#
#++++++++++++++++++++ Streamlit app +++++++++++++++++++++++++++++


st.title("IGBC Guidelines Retrieval App")
st.markdown("**Search for information in the IGBC Green New Buildings Rating System guidelines.**")

# Add a sidebar for credit selection
st.sidebar.header("Filter by Credit (Optional)")
selected_credit = st.sidebar.selectbox("Select a credit:", ["All"] + credit_words)

# Input
query = st.text_input("Enter your query:")

# Retrieve and show results
if query:
    retrieved_chunks = retrieve_relevant_chunks(vectorstore, query, selected_credit)

    if retrieved_chunks:
        st.header("Results:")
        for chunk in retrieved_chunks:
            st.markdown(f"**Credit:** {chunk.metadata['credit']}, **Page:** {chunk.metadata['page']}")
            st.write(chunk.page_content)
            st.write("---")
    else:
        st.info("No relevant chunks found for your query.")


st.markdown("---")
st.markdown("**Source:** IGBC Green New Buildings Rating System V3.0")