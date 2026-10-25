# ScamSHIELD — SMS Scam Detection System

## 1. Project Overview

ScamSHIELD is a machine learning-based web application that classifies SMS messages as **Spam** (potentially suspicious) or **Not Spam** (normal message).

The application uses TF-IDF for text feature extraction and Logistic Regression for classification. A Flask backend connects the trained machine learning model to a web interface.

## 2. Project Objectives

- Detect potentially suspicious SMS messages.
- Classify messages as Spam or Not Spam.
- Display prediction results through a simple website.
- Demonstrate the integration of Machine Learning with Flask.

## 3. Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas and NumPy
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- HTML and CSS

## 4. Project Structure

```text
scamSHILD final 2.3/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── dataset/
│   └── spam.csv
├── models/
│   ├── scam_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── scam_model_backup.pkl
│   └── tfidf_vectorizer_backup.pkl
├── notebook/
│   ├── scamSHILD_final.ipynb
│   └── models/
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## 5. What Each File Does

- `app.py`: Runs the Flask application and handles message predictions.
- `templates/index.html`: Contains the website form and result interface.
- `static/style.css`: Controls the website's appearance and layout.
- `models/scam_model.pkl`: Stores the trained classification model.
- `models/tfidf_vectorizer.pkl`: Converts message text into TF-IDF features.
- `models/scam_model_backup.pkl`: Backup copy of the classification model.
- `models/tfidf_vectorizer_backup.pkl`: Backup copy of the vectorizer.
- `dataset/spam.csv`: Contains the SMS dataset used by the project.
- `notebook/scamSHILD_final.ipynb`: Contains the machine learning workflow.
- `requirements.txt`: Lists the Python package dependencies.
- `.gitignore`: Specifies files and folders Git should ignore.

## 6. Machine Learning Workflow

1. Load and prepare the SMS dataset.
2. Split the data into training and testing sets.
3. Convert message text into TF-IDF features.
4. Train a Logistic Regression classifier.
5. Evaluate the model using classification metrics.
6. Save the trained model and vectorizer.
7. Load the saved artifacts in Flask.
8. Transform user-entered messages and generate predictions.

## 7. Model Evaluation

Reported test results:

- **Accuracy:** 98.71%
- **Spam Precision:** 95%
- **Spam Recall:** 95%
- **Spam F1-score:** 95%



## 8. How to Run the Project

### Prerequisites

- Python installed on the system.
- The project files and saved model artifacts available locally.

### Installation

1. Open the project folder in VS Code.

2. Open Terminal → New Terminal.

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt 
   ```

4. Start the Flask application:

   ```bash
   python app.py
   ```

5. Open the following address in your browser:

   `http://127.0.0.1:5000`

6. Enter an SMS message and submit it to view the prediction.

**Note:** The scikit-learn version used to load the saved model should be compatible with the version used to create it.

## 9. Limitations

- Predictions are not guaranteed to be correct.
- Unseen messages may be classified incorrectly.
- Model performance depends on the quality and coverage of the training data.
- The model may not recognize every new or evolving scam pattern.
- Dependency and model-version compatibility should be verified before deployment.

## 10. Disclaimer

ScamSHIELD provides machine learning-based predictions for educational and demonstration purposes. Its predictions should not be treated as a guarantee that a message is safe or fraudulent.
