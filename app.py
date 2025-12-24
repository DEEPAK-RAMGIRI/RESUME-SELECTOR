from dotenv import load_dotenv
load_dotenv()
from io import BytesIO
import base64
import streamlit as st
import os
from google import genai
from pdf2image import convert_from_bytes


client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))


def genearte_response(inputs,pdf_content,prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": f"JOB DESCRIPTION:\n{inputs}\n\n{prompt}"},
                    {
                        "inline_data": {
                            "mime_type": pdf_content[0]["mime_type"],
                            "data": pdf_content[0]["data"]
                        }
                    }
                ]
            }
        ]
        )
    return response.text

def pdftoimagetobase64Conversion(file):
    if file:
        images = convert_from_bytes(file.read(),poppler_path=r"C:\Program Files\poppler-25.12.0\Library\bin")
        page1 = images[0]
        
        buffer = BytesIO()# a buffer which store the data  temparay in variable instead of storing it in disk 
        page1.save(buffer, format="JPEG")
        buffer = buffer.getvalue()

        pdf_content = [
            {
                "mime_type" : "image/jpeg",
                "data" :base64.b64encode(buffer).decode()
            }
        ]

        return pdf_content
    else:
        raise FileNotFoundError("No File Uploaded 😲")
    
    
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to top, #141e30 0%, #243b55 100%) !important;
        background-attachment: fixed;
        color: white; /* optional: make text readable */
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
st.title("RESUME SELECTOR")
text = st.text_area("job description",key = "input")
file = st.file_uploader("upload your resume")
if file:
    st.write("PDF Uploaded")
    

s1 = st.button("Summerize")

s2 = st.button("Score")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""


if s1:
    if file:
        response = genearte_response(text,pdftoimagetobase64Conversion(file),input_prompt1)
        st.write(response)
if s2:
    if file:
        response = genearte_response(text,pdftoimagetobase64Conversion(file),input_prompt2)
        st.write(response)