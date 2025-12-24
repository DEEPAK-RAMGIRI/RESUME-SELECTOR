# RESUME-SELECTOR

Resume Selector is a Streamlit-based web application that evaluates a candidate’s resume against a given job description using LLM-based analysis.
It simulates an ATS (Applicant Tracking System) to provide a match score, missing keywords, strengths, weaknesses, and improvement suggestions

**Live Demo:** Not available for now 😔

[!Screenshot]()

**Tech Stack:**

*  Streamlit – UI
* Google Gemini – Resume evaluation
* pdf2image – PDF processing
* Pillow – Image handling
* Python-dotenv – Environment variable management

**Features**
* Upload resume in PDF format
* Convert PDF → Image → Base64
* Analyze resume using LLM (Gemini)
    * Get:
          Resume summary
          ATS match percentage
          Missing keywords
          Improvement suggestions


### INSTALLING

**Clone the repository**
```
git clone https://github.com/your-username/resume-selector.git
cd resume-selector
```
**Create virtual environment (optional)**
```
python -m venv venv
venv\Scripts\activate   # Windows
```
**Install dependencies**
```
pip install -r requirements.txt
```

**Create a .env file in the root directory:**
get ur [API HERE:](https://aistudio.google.com/apikey?_gl=1*9jchcg*_ga*OTMyMDY4NzA0LjE3NTczMjM2ODA.*_ga_P1DBVKWT6V*czE3NTgyNTgwMTYkbzIkZzAkdDE3NTgyNTgwMTYkajYwJGwwJGgxMjkxNTI0ODg5)  
```
GOOGLE_API_KEY=your_gemini_api_key
```

### Dont forget setup poppler according to U r Operating System

```
streamlit run app.py
```
**Working:**
```
Job Description (Text)
        ↓
Resume PDF Upload
        ↓
PDF → Image → Base64
        ↓
Gemini LLM Analysis
        ↓
ATS Score + Feedback

```
### FOLDER STRCTURE
```
RESUME-SELECTOR/
│── app.py                     # main File
│── requirements.txt           # Project dependencies
│── .gitignore                 # Ignored files/folders
└──  README.md                 # Documentation

```



