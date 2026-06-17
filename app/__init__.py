import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

experiences = [
    {
        "role": "Senior Office Assistant",
        "company": "Associated Students – San Francisco State University",
        "dates": "Aug 2024 - Present",
        "bullets": [
            "Built end-to-end automation pipelines using Make.com, Zapier, and Azure OCR for receipt data extraction, cutting manual processing time by 40% and increasing audit accuracy.",
            "Architected a Notion ecosystem tracking document approvals and lifecycle logic across 10 departments, replacing fragmented spreadsheet workflows.",
        ],
    },
    {
        "role": "Volunteer Workflow Automation Assistant",
        "company": "Mercy Clinic",
        "dates": "June 2025 - July 2025",
        "bullets": [
            "Automated quarterly medicine credit reconciliation using Make.com and Zapier, cutting manual Excel comparisons by 60% and increasing data reliability.",
        ],
    },
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), experiences=experiences)
