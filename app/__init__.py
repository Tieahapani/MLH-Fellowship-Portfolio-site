import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies)
