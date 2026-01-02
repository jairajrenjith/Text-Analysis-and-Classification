# Text Analysis and Classification using Machine Learning

This project demonstrates two core Natural Language Processing (NLP) tasks using Python:

1. Rule-Based Resume Information Extraction  
2. Sentiment Analysis and Classification using Machine Learning  

The project is designed for beginners and explains the complete workflow from raw text processing to model training, evaluation, and comparison.

---

## Project Structure

```
Text_Analysis_and_Classification/
│
├── resume_extractor/
│   ├── extractor.py
│   ├── resumes.txt
│   └── output.json
│
├── sentiment_analysis/
│   ├── dataset.csv
│   └── sentiment_analysis.ipynb
│
├── requirements.txt
└── README.md
```

Note: The virtual environment (`venv/`) is intentionally not included.  
It should be created locally after cloning the project.

---

## Objective 1: Resume Information Extractor (Rule-Based)

### Purpose
To extract email addresses and phone numbers from resume text using rule-based techniques (regular expressions), without using any machine learning models.

### Input
- `resumes.txt`: Contains resume details of multiple people written in different formats.

### How It Works
- Reads the resume text file
- Uses regex patterns to identify valid email addresses
- Uses regex patterns to identify valid Indian phone numbers
- Removes duplicate entries
- Saves extracted data in structured JSON format

### Output
- `output.json`: Structured file containing extracted emails and phone numbers

### How to Run
```bash
cd resume_extractor
python extractor.py
```

---

## Objective 2: Sentiment Classification on Custom Dataset

### Purpose
To train and evaluate multiple sentiment classification models using traditional machine learning techniques and compare their performance.

### Dataset
- `dataset.csv`
- Columns used:
  - `review`: Text data
  - `sentiment`: Sentiment labels (positive / negative / neutral)

---

## Sentiment Analysis Workflow

### Data Loading
- Dataset is loaded using Pandas
- Column names are verified before processing

### Text Preprocessing
- Convert text to lowercase  
- Remove punctuation  
- Tokenize text into words  
- Remove stopwords using NLTK  
- Store cleaned text in a new column called `clean_text`

### Baseline Sentiment Analysis
- Uses TextBlob to compute sentiment polarity
- Serves as a rule-based baseline for comparison

### Feature Extraction
- Converts text into numerical form using TF-IDF Vectorization

### Model Training
The following models are trained:
- Naive Bayes  
- Support Vector Machine (SVM)  
- Random Forest  

### Model Evaluation
Models are evaluated using:
- Accuracy  
- Precision  
- Recall  
- F1 Score  

### Visualization
- Bar chart comparison of all model performances
- Confusion matrix for the SVM model

---

## Libraries and Tools Used

- Python 3.11  
- Pandas  
- NLTK  
- TextBlob  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

All dependencies are listed in `requirements.txt`.

---

## Environment Setup (After Cloning)

### Create Virtual Environment

  ```bash
  python -m venv venv
  ```

### Activate Virtual Environment

a. Windows:
  ```bash
  venv\Scripts\activate
  ```

b. Linux / macOS:
  ```bash
  source venv/bin/activate
  ```

### Install Dependencies

  ```bash
  pip install -r requirements.txt
  ```

### Download Required NLP Resources

  ```bash
  python -m nltk.downloader punkt stopwords
  python -m textblob.download_corpora
  ```

---

## Running Sentiment Analysis

  ```bash
  cd sentiment_analysis
  jupyter notebook
  ```

Open `sentiment_analysis.ipynb` and run all cells sequentially from top to bottom.

---

## Project Outcomes

- Extracted resume contact information using rule-based NLP techniques  
- Built and compared multiple sentiment classification models  
- Learned the complete NLP pipeline from raw text to evaluation  
- Gained hands-on experience with TF-IDF and ML classifiers  

---

## Use Cases

- Resume parsing systems  
- HR automation tools  
- Customer feedback analysis  
- Product review sentiment analysis  
- Educational NLP and ML projects  

---

## Notes

- This project is intended for educational purposes only  
- Dataset column names may vary and should be verified before processing  
- Python 3.11 is recommended for maximum library compatibility  
- Virtual environments are not included and should be created locally  

---

## Author

Jairaj R  
Email: jairajrenjith@gmail.com
