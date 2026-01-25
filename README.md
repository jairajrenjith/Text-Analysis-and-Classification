# Text Analysis and Classification using Machine Learning

Rule-based resume parser and machine learning sentiment analysis project using NLP, TF-IDF, and classification models (Naive Bayes, SVM, Random Forest).

---

## Project Overview

This project contains two main components:

### 1. Resume Information Extractor (Rule-Based NLP)

A Python script that extracts structured information from resume text files:
- Name  
- Role / Job Title  
- Email Addresses  
- Phone Numbers  

The extracted data is saved in a structured **JSON** format.

### 2. Sentiment Classification on IMDB Reviews

A machine learning pipeline that classifies movie reviews as **positive** or **negative** using:
- Text preprocessing
- TF-IDF feature extraction
- Multiple ML models for comparison

---

## Project Structure

```
text_analysis_project/
│
├── resume_extractor.py        # Rule-based resume parser
├── sentiment_analysis.ipynb   # ML sentiment classification notebook
├── IMDB Dataset.csv           # Sentiment dataset (reviews + sentiment)
├── requirements.txt           # Required Python libraries
├── output.json                # Extracted resume results (generated)
│
└── resumes/                   # Sample resume text files
    ├── resume1.txt
    ├── resume2.txt
    └── resume3.txt
```

---

## Installation

Make sure Python 3.8+ is installed.

### 1. Clone the repository

  ```bash
  git clone https://github.com/your-username/text_analysis_project.git
  ```

### 2. Navigate into the project folder

  ```bash
  cd text_analysis_project
  ```

### 3. Create virtual environment

  ```bash
  python -m venv venv
  ```

### 4. Activate virtual environment

  a. Windows:

  ```bash
  venv\Scripts\activate
  ```

  b. macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

### 5. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

---

## How to Run

### 1. Run Resume Extractor

  ```bash
  python resume_extractor.py
  ```

This reads all `.txt` files inside the `resumes/` folder and generates `output.json`. 
This contains extracted name, role, emails, and phone numbers.

---

### 2. Run Sentiment Analysis

  ```bash
  jupyter notebook sentiment_analysis.ipynb
  ```

Then run all cells to:
- Clean text data
- Convert text to TF-IDF features
- Train ML models (Naive Bayes, SVM, Random Forest)
- Evaluate using Accuracy, Precision, Recall, and F1-score
- Visualize performance using confusion matrices and bar charts

---

## Models Used

- Multinomial Naive Bayes  
- Support Vector Machine (Linear SVM)  
- Random Forest Classifier  
- TextBlob (Baseline Sentiment)

---

## Evaluation Metrics

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix Visualization  

---

## Technologies Used

- Python  
- Regular Expressions (Regex)  
- Pandas & NumPy  
- Scikit-learn  
- NLTK  
- TextBlob  
- Matplotlib & Seaborn  

---

## Key Features

✔ Rule-based resume parsing  
✔ Generic phone number detection  
✔ Email extraction  
✔ Machine learning text classification  
✔ Model comparison and visualization  
✔ Reproducible project setup  

---

## Output Example (Resume Extractor)

```json
{
  "resume1.txt": {
    "name": "John Doe",
    "role": "Software Developer",
    "emails": ["john.doe@gmail.com"],
    "phone_numbers": ["+1-202-555-0173"]
  }
}
```

---

## License

This project is for academic and learning purposes.

---

By Jairaj R.
