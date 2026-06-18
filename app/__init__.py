import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

pages = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"},
]


@app.context_processor
def inject_pages():
    return dict(pages=pages)

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

hobbies = [
    {
        "name": "Early Morning Walks",
        "description": "Taking early morning walks calms me down and helps me start the day fresh.",
    },
    {
        "name": "Listening to Podcasts",
        "description": "I love tuning into podcasts to learn new things and hear different perspectives.",
    },
    {
        "name": "Trying New Foods",
        "description": "Exploring different cuisines and flavors is one of my favorite things to do.",
    },
    {
        "name": "Building Projects & Learning New Skills",
        "description": "I enjoy building new projects and constantly picking up new skills to grow as a developer.",
    },
]

locations = [
    {"name": "New Zealand", "lat": -40.9006, "lng": 174.886, "note": "An amazing adventure"},
    {"name": "South Africa", "lat": -30.5595, "lng": 22.9375, "note": "Saw the famous safari!"},
    {"name": "Chicago, USA", "lat": 41.8781, "lng": -87.6298, "note": "Best place I have visited so far"},
    {"name": "Lapland, Finland", "lat": 68.0, "lng": 26.0, "note": "Dream destination — I really want to see the northern lights!"},
]


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow",
        url=os.getenv("URL"),
        experiences=experiences,
        education=education,
        hobbies=hobbies,
        locations=locations,
    )


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies)
