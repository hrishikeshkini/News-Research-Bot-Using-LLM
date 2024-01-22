# FinScribe : News Research Bot Using LLM

## Table of Content
  * [Demo](#demo)
  * [Problem Statement](#problem-statement)
  * [Approach](#approach)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployement](#deployement)
  * [Detailed Project Reports](#detailed-project-reports)
  * [Bugs & Logs](#bugs--logs)
  * [Contributors](#contributors)

## Demo
Link: [personal-analyst.onrender.com](personal-analyst.onrender.com)


## Screenshots
![Screenshot](Capture.PNG)
![Screenshot](Capture2.PNG)
![Screenshot](Capture3.PNG)


## Problem Statement
#### NewsAnalyzer: Uncover Financial Insights from News Articles

Equity research analysts often face challenges in efficiently extracting key insights from a vast array of financial news articles. The abundance of data requires a tool that can quickly analyze news content, provide relevant insights, and engage in a dynamic conversation to streamline the research process.

#### PDFChatBot: Extract Knowledge from Financial PDFs with Ease 

Equity research analysts encounter difficulties when dealing with extensive financial PDF documents. Manually extracting and interpreting information from these documents is time-consuming. There is a need for a tool that allows analysts to effortlessly upload financial PDFs, ask specific questions, and receive detailed responses through a conversational interface, facilitating quicker and more effective research.

## Approach
Document Parsing : Implement a PDF parsing mechanism to extract text content from financial PDF documents and data from website using urls.
Handle various document structures, tables, and formats commonly found in financial reports.

Text Embeddings : Utilize pre-trained language models to generate embeddings for the extracted text.
Choose models that capture semantic relationships and context in financial documents.

Vector Store : Build a vector store using technologies like FAISS to index and search through document embeddings efficiently.
Optimize for quick retrieval of relevant documents based on user queries.

Conversational AI : Integrate a conversational AI model that understands user questions and context within financial documents.
Enable users to ask questions about specific sections of the document and receive accurate responses.

User-Friendly Interface : Develop a user-friendly interface for uploading PDFs, Uploading URLs, asking questions, and viewing responses.
Include features for navigating through document sections and exploring related information.

Deployment :  Created an UI with a form that takes all the necessary inputs from user and shows the output. After that I have deployed project on render using github with versioning control.


## Technologies Used
 
   1. Python 
   2. Web Scraping
   3. Langchain
   4. OpenAI 
   5. Google Gemini Pro
   6. Render cloud
   7. PDF Parsing
   8. Streamlit

## Installation
Click here to install [python](https://www.python.org/downloads/). To install the required packages and libraries, run this pip command in the project directory after cloning the repository:
```bash
git clone https://github.com/hrishikeshkini/News-Research-Bot-Using-LLM.git
pip install -r requirements.txt
```
If pip is not already installed, Follow this [link](https://pip.pypa.io/en/stable/installation/)

## Deployement
Create a web service on render cloud servide. You can either connect your github profile to manually deploy this project or Also we can deploy our docker image.
Follow the instruction given on [Render Documentation](https://docs.render.com/) to deploy a web app.

## Bugs & Logs

1. If you find a bug, kindly open an issue and it will be addressed as early as possible. [Open](https://github.com/hrishikeshkini/News-Research-Bot-Using-LLM/issues)
2. Under localhost, logging is performed for all the actions and its stored onto logs.txt file
3. When the app is deployed on render, logs can be viewed on  render dashboard or CLI.

## Contributors
  [Hrishikesh Kini](https://github.com/hrishikeshkini)
