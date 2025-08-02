from flask import Flask, render_template, request
import fitz  # PyMuPDF
import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")  # 🆕 Use your Groq key here

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    uploaded_file = request.files['resume']
    jd_text = request.form.get('jd', '')

    if uploaded_file.filename != '':
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
        uploaded_file.save(filepath)

        # Extract resume text
        doc = fitz.open(filepath)
        resume_text = ""
        for page in doc:
            resume_text += page.get_text()

        # 📌 Prompt with JD Match logic
        prompt = f"""
You are an expert resume reviewer.

Compare the following resume with the given Job Description (JD):

Resume:
{resume_text}

JD:
{jd_text}

Give a JD match score out of 100 and bullet point suggestions to improve the match. Format your response like this:

JD Match Score: 85

Suggestions:
- Add more keywords related to X
- Mention experience in Y
- Improve section on Z
"""

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama3-8b-8192",  # ✅ Use stable Groq model
            "messages": [{"role": "user", "content": prompt}]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
        else:
            result = "Something went wrong with the AI API."

        return render_template('result.html', result=result)

    return "No file uploaded"

# if __name__ == '__main__':
    # app.run(debug=True)
