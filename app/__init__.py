import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

education = [
    {
        "school": "San Francisco State University",
        "degree": "Bachelor's Degree",
        "dates": "Expected May 2027",
        "details": "Studied Data Structures and Algorithms, Operating Systems, and Programming Methodology. Also pursuing AI courses and attending workshops.",
    },
    {
        "school": "Lourdes Convent",
        "location": "Surat, Gujarat, India",
        "degree": "High School",
        "dates": "Completed",
        "details": "",
    },
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), education=education)
