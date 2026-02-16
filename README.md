# Anti-Phishing URL Detection System

## Overview
This project implements a feature-based machine learning system to detect phishing URLs. 
The system analyses structural and lexical characteristics of URLs and classifies them as phishing or legitimate.

## Features Extracted
- URL length
- Number of dots and hyphens
- Presence of HTTPS
- IP-based URL detection
- Suspicious keyword count
- URL entropy

## Dataset
- 400 URLs
- Balanced dataset
- Version: dataset_v1
- Includes IP-based phishing examples

## Machine Learning Models
- Logistic Regression
- 80/20 train-test split
- Evaluation using accuracy, precision, recall

## Explainability
The system provides human-readable explanations for phishing predictions based on extracted features.

## Technologies Used
- Python
- Pandas, NumPy
- scikit-learn
- Streamlit

## How to Run
1. Install dependencies  
   `pip install -r requirements.txt`
2. Build dataset
    `py -3.11 src/build_dataset.py`
3. Open Notebook
   `train_model.ipynb`

## Model Performance
- Accuracy: 98.75%
- Precision: 1.0
- Recall: 0.978

5-fold Cross Validation Accuracy: ~0.98

## Limitations
This project uses lexical features only.
It does not inspect webpage content, domain age, or SSL certificates.

## Future Scope
- Incorporate content-based analysis (HTML, JavaScript inspection).
- Add domain metadata features such as WHOIS age and SSL validation.
- Evaluate advanced ML models including Random Forest and Gradient Boosting.
- Develop a real-time detection API and browser extension integration  
- Email phishing detection  