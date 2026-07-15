# Fake Job Posting Analyzer 🔍

## 📌 Project Overview

Fake Job Posting Analyzer is a Data Science and Machine Learning project that identifies fraudulent job postings from online job advertisements.

The project analyzes job posting details such as company information, job description, requirements, employment type, location, and other features to predict whether a job posting is genuine or fraudulent.

The goal of this project is to help job seekers avoid scams and improve trust in online recruitment platforms.

---

## 🚀 Features

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Missing Value Analysis
* Text Data Analysis
* Feature Engineering
* Data Visualization
* Machine Learning Model Training
* Fraudulent Job Prediction
* Interactive Streamlit Dashboard

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* NumPy → Numerical computations
* Pandas → Data manipulation and analysis
* Matplotlib → Data visualization
* Seaborn → Statistical visualization
* Plotly → Interactive visualizations
* Scikit-learn → Machine Learning algorithms
* Streamlit → Web application development
* Joblib → Model serialization

---

## 📂 Project Structure

```
Fake-Job-Posting-Analyzer/

│
├── app.py                         # Streamlit application
├── fake_job_analyzer.ipynb        # Data analysis and model development
├── model.pkl                      # Trained machine learning model
├── requirements.txt               # Required Python libraries
├── README.md                      # Project documentation
│
└── dataset/
    └── fake_job_postings.csv      # Dataset
```

---

## 📊 Dataset

The dataset contains information about job advertisements with features such as:

* Job Title
* Location
* Department
* Salary Range
* Company Profile
* Job Description
* Requirements
* Benefits
* Employment Type
* Required Experience
* Required Education
* Industry
* Function
* Fraudulent Label

Target Variable:

```
fraudulent
```

* 0 → Genuine Job Posting
* 1 → Fraudulent Job Posting

---

## 🔎 Exploratory Data Analysis

Performed analysis includes:

* Missing value percentage analysis
* Distribution of fraudulent and genuine jobs
* Feature relationship analysis
* Categorical feature analysis
* Text length analysis
* Visualization using Matplotlib, Seaborn and Plotly

---

## ⚙️ Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Prediction using Streamlit Application

---

## 🤖 Machine Learning Model

The model is trained to classify job postings into:

* Genuine Job
* Fake Job

Evaluation metrics:

* Accuracy Score
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🖥️ Streamlit Application

The project includes an interactive web application where users can enter job posting details and get predictions.

Run the application:

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

* Use advanced NLP techniques for text analysis
* Implement Deep Learning models
* Add real-time job posting verification
* Deploy using cloud platforms
* Improve prediction accuracy

---

## 👩‍💻 Author

**Garima Gupta**

## ⭐ If you find this project useful, consider giving it a star!
