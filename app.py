
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained ML model and TF-IDF vectorizer
model = joblib.load("models/scam_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_message():
    message = request.form.get("message", "").strip()

    # Empty message validation
    if not message:
        result = {
            "detection": "Please enter your message",
            "chance": "",
            "probability": "",
            "result_type": "neutral"
        }

        return render_template("index.html", result=result)

    # Convert message into TF-IDF features
    message_vector = vectorizer.transform([message])

    # Predict HAM or SPAM
    prediction = model.predict(message_vector)[0]

    # Calculate spam probability
    probabilities = model.predict_proba(message_vector)[0]
    spam_index = list(model.classes_).index("spam")
    spam_probability = probabilities[spam_index] * 100

    # Detection result
    if prediction == "spam":
        detection = "SPAM"
        result_type = "spam"
    else:
        detection = "NOT SPAM"
        result_type = "ham"

    # Chance level
    if spam_probability >= 80:
        chance = "High Chance"
    elif spam_probability >= 40:
        chance = "Normal Chance"
    else:
        chance = "Low Chance"

    result = {
        "detection": detection,
        "chance": chance,
        "probability": f"{spam_probability:.2f}%",
        "result_type": result_type
    }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
