from flask import Flask, request, jsonify, render_template
from resume_generator import generate_summary

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    resume_json = request.get_json()
    summary_text = generate_summary(resume_json)
    return jsonify({'summary': summary_text})

if __name__ == "__main__":
    print("Device set to use cpu")
    app.run(debug=True)
