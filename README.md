# 🧠 AI Resume Summary Generator

An AI-powered resume summarizer built with **Flask** and **Hugging Face Transformers** that generates concise, professional summaries from structured resume data (JSON input).  
Ideal for quick candidate profiling and HR automation.

https://github.com/NewAi25/resume-system-trial-task/blob/5ca74ee9389e3cebf822588a4798887b987aa72c/Screenshot%202025-10-29%20124454.png

---

## 🚀 Features

- Summarizes structured resume data into 1–2 professional sentences  
- Built using **facebook/bart-large-cnn**
- Flask-based lightweight backend for easy local or cloud deployment  
- Runs smoothly on CPU — no GPU required  

---

## 🧩 Tech Stack

- **Backend:** Python (Flask)  
- **AI Model:** Hugging Face Transformers (BART)  
- **Frontend:** HTML, CSS  
- **Environment:** Virtualenv  
- **Hosting Options:** Hugging Face Spaces / AWS Free Tier / Localhost  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/NewAi25/resume-system-trial-task.git
cd resume-system-trial-task
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
3. Activate the Virtual Environment
Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run the Application
python app.py

6. Access the App
Once the Flask server starts, open your browser and visit:
👉 http://127.0.0.1:5000

🧠 Example Input (JSON)
json
{
  "name": "John Doe",
  "education": "B.Tech in Computer Science, IIT Delhi",
  "experience": "3 years as a DevOps Engineer at AWS",
  "skills": ["Docker", "Kubernetes", "CI/CD", "Python"]
}
🔍 Example Output
John Doe, a Computer Science graduate from IIT Delhi with 3 years of experience in DevOps, skilled in Docker, Kubernetes, and CI/CD automation.
📁 Project Structure

resume-system-trial-task/
│
├── app.py                # Flask app (main file)
├── resume_generator.py   # Hugging Face AI logic
├── templates/
│   └── index.html        # Simple web UI
├── static/
│   └── style.css         # Styling
├── requirements.txt
└── .env                  # Optional (for Hugging Face token)
💡 Deployment Tips
You can deploy this app for free on:

Hugging Face Spaces 

AWS Free Tier EC2 / Elastic Beanstalk

Render / Railway / Deta Space

For best results, use a CPU-based summarization model like:
facebook/bart-large-cnn
📘 Author
Manisha Sarkar
🔗 GitHub: NewAi25
💬 Built as part of an AI resume summarization system prototype.

