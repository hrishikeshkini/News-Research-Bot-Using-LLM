# FinSCribe : News Research Bot Using LLM

## Table of Content
  * [Demo](#demo)
  * [Problem Statement](#problem-statement)
  * [Approach](#approach)
  * [Technologies Used](#technologies-used)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
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
** NewsAnalyzer: Uncover Financial Insights from News Articles **

Equity research analysts often face challenges in efficiently extracting key insights from a vast array of financial news articles. The abundance of data requires a tool that can quickly analyze news content, provide relevant insights, and engage in a dynamic conversation to streamline the research process.

** PDFChatBot: Extract Knowledge from Financial PDFs with Ease **

Equity research analysts encounter difficulties when dealing with extensive financial PDF documents. Manually extracting and interpreting information from these documents is time-consuming. There is a need for a tool that allows analysts to effortlessly upload financial PDFs, ask specific questions, and receive detailed responses through a conversational interface, facilitating quicker and more effective research.

## Approach
Data Exploration : I started exploring dataset using pandas,numpy,matplotlib and seaborn.

Data visualization : Ploted graphs to get insights about dependend and independed variables.

Feature Engineering : Removed missing values and created new features as per insights.

Model Building & Testing : Tried many machine learning algorithms and checked the base accuracy to find the best fit.

User Interface & deployment :  Created an UI with a form that takes all the necessary inputs from user and shows the output.
                          After that I have deployed project on heroku. The model has been deployed on ibm cloud machine learning.
## Technologies Used
 
   1. Python 
   2. Sklearn
   3. Tensorflow
   4. Pandas, Numpy 
   5. Streamlit
   6. heroku cloud
   7. ibm cloud

## Dataset
[Download here](https://www.kaggle.com/adityakadiwal/water-potability/download)

## Installation
Click here to install [python](https://www.python.org/downloads/). To install the required packages and libraries, run this pip command in the project directory after cloning the repository:
```bash
git clone https://github.com/hrishikeshkini/Water-Quality-Drinking-water-potability.git
pip install -r requirements.txt
```
If pip is not already installed, Follow this [link](https://pip.pypa.io/en/stable/installation/)

## Deployement on Heroku
Create a virtual app on Heroku website. You can either connect your github profile or download cli to manually deploy this project.
Follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Bugs & Logs

1. If you find a bug, kindly open an issue and it will be addressed as early as possible. [Open](https://github.com/hrishikeshkini/Water-Quality-Drinking-water-potability/issues)
2. Under localhost, logging is performed for all the actions and its stored onto logs.txt file
3. When the app is deployed on heroku, logs can be viewed on  heroku dashboard or CLI.

## Contributors
  [Hrishikesh Kini](https://github.com/hrishikeshkini)
