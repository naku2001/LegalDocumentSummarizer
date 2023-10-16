# Insightful Analytics App

Welcome to the Insightful Analytics App! This app allows you to summarize, analyze sentiment, perform entity recognition, and answer questions based on text or document data. You can either manually input text or upload a document for analysis.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.10
- pip (Python package manager)

## Installation

1. Clone this repository or download the source code to your local machine.

```bash
git clone <repository_url>
```

2. Navigate to the project directory.

```bash
cd Insightful-Analytics-App
```

3. Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

## Usage

1. Set up your OpenAI API key:

   - Create an account and obtain an API key from [OpenAI](https://beta.openai.com/signup/).
   - Store your API key in a .env file in the project directory:

   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

2. Launch the Streamlit application:

```bash
streamlit run app.py
```

3. The app will open in your default web browser. You can now use it to analyze text or documents.

## Features

### 1. **Manually Input Text**

Choose the "Manually Input Text" option to enter your own text for analysis.

### 2. **Upload a Document**

Choose the "Upload a Document" option to upload a document (in TXT, PDF, or DOCX format) for analysis. This input methods have the following features:

#### a. Review Document

- Click the "Review Document" button.
- The app will provide you with a quick preview of the uploaded document, displaying the first few words.

#### b. Sentiment Analysis

- Click the "Sentiment Analysis" button.
- The app will analyze the sentiment of the uploaded document and provide a sentiment score.

#### c. Entity Recognition

- Click the "Entity Recognition" button.
- The app will identify and display entities, names, and locations found in the uploaded document.

#### d. Ask Questions

- Enter your question in the "Ask a question on information in the document" input box.
- Click the "Answer Question" button.
- The app will provide you with an answer to your question based on the uploaded document.

#### e. Summarize Document

- Click the "Summarize Document" button.
- The app will generate a summary of the uploaded document, highlighting key points and main ideas.

#### f. Download Summary as PDF

- After summarizing the document, click the "Download Summary as PDF" button.
- The app will generate a PDF document containing the summary for download.

#### g. Download Summary as Word

- After summarizing the document, click the "Download Summary as Word" button.
- The app will generate a Word document containing the summary for download.

## Development

If you'd like to contribute to the development of this application, feel free to fork the repository, make your changes, and submit a pull request.

## Note

Before using the application, make sure you have a valid OpenAI API key, and you've created an `.env` file in the project directory with the `OPENAI_API_KEY` variable.

## Contact

For questions or support, please contact [Perfect-Princess Makuwerere](mailto:janedoe@email.com) or [Anesu Rirwa](mailto:anerirwa@email.com).

Happy analyzing!
```