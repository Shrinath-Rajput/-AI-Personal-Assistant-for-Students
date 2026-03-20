from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import os

from utils.resume import analyze_resume
from utils.chatbot import chatbot_response

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, 'model/performance_model.pkl'), 'rb'))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    hours = float(data['hours'])
    attendance = float(data['attendance'])

    result = model.predict([[hours, attendance]])
    return jsonify({"marks": round(result[0], 2)})

@app.route('/resume', methods=['POST'])
def resume():
    text = request.json['resume']
    score = analyze_resume(text)
    return jsonify({"score": score})

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json['message']
    reply = chatbot_response(msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)