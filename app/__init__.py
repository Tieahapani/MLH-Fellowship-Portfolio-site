import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

locations = [
    {"name": "New Zealand", "lat": -40.9006, "lng": 174.886, "note": "An amazing adventure"},
    {"name": "South Africa", "lat": -30.5595, "lng": 22.9375, "note": "Saw the famous safari!"},
    {"name": "Chicago, USA", "lat": 41.8781, "lng": -87.6298, "note": "Best place I have visited so far"},
    {"name": "Lapland, Finland", "lat": 68.0, "lng": 26.0, "note": "Dream destination — I really want to see the northern lights!"},
]


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), locations=locations)
