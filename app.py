import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Function for document summarization
def document_summarization(document_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Summarize the following legal document:\n{document_text}",
        max_tokens=150
    )
    return response.choices[0].text

# Streamlit UI
st.title("Legal Document Summarizer")

uploaded_file = st.file_uploader("Upload a legal document (TXT or PDF)", type=["txt", "pdf"])

if uploaded_file is not None:
    file_content = uploaded_file.read()

    if uploaded_file.type == "text/plain" or uploaded_file.type == "application/pdf":
        st.subheader("Uploaded Document:")

        # Display the first few words of the document when 'Review' button is clicked
        if st.button("Preview Document"):
            first_few_words = " ".join(file_content.decode("utf-8").split()[:50])  # Show first 50 words
            st.write(first_few_words + "...")
        
        if st.button("Summarize"):
            st.subheader("Summary:")
            summary = document_summarization(file_content.decode("utf-8"))
            st.write(summary)
    else:
        st.warning("Invalid file format. Please upload a TXT or PDF file.")
