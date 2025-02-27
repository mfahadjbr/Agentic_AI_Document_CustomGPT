import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from google.api_core.exceptions import ResourceExhausted

# Set the page configuration
st.set_page_config(
    page_title="CustomGPT For Agentic AI Document",
    page_icon="📚"
)

# Add a title and description
st.title("📚 CustomGPT For Agentic AI Document")
st.write("Ask questions about the content of the document. Here are some example questions you can try:")
st.markdown("- What is the main topic of this document?")
st.markdown("- Explain the most important concepts mentioned?")
st.link_button("Click here to open Agentic AI Document", "https://docs.google.com/document/d/15usu1hkrrRLRjcq_3nCTT-0ljEcgiC44iSdvdqrCprk/edit?tab=t.0")
st.markdown("---")


# Initialize the PDF loader with the file path
loader = PyPDFLoader("agentic_ai.pdf")
# Load and split the document into individual pages
pages = loader.load_and_split()
document = loader.load()
# User input section
with st.container():
    user_input = st.text_area("Enter your question:", placeholder="Type your question here...", height=100)
    submit_button = st.button("Get Answer", type="primary")



llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key="AIzaSyAnccZ0sAKJaAiVT4vTpYgiqT_0BQ0rvQQ")
prompt  =  f""" 
           You have to response  the user {user_input} according to the provided document 
           document {document},

           if the user query dont match the document, then response with sorry 

"""

if submit_button and user_input:
    with st.spinner("Analyzing document and generating answer..."):
        response = llm.invoke(prompt)
        st.markdown("---")
        st.markdown("### 📝 Answer:")
        st.text_area("Response:", value=response.content, height=300)
        st.success("Response generated successfully!")
elif submit_button and not user_input:
    st.warning("Please enter a question before submitting.")