import os
import hashlib
import datetime
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING" ) == "true" :
    print( "Running DB in test mode")
    myportfoliodb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    myportfoliodb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306
)

print(myportfoliodb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = myportfoliodb

myportfoliodb.connect()
myportfoliodb.create_tables([TimelinePost])



pages = [
    {"name": "Home", "url": "/"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Timeline", "url": "/timeline"},
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
        "image": "hobby_walks.jpg",
    },
    {
        "name": "Listening to Podcasts",
        "description": "I love tuning into podcasts to learn new things and hear different perspectives.",
        "image": "hobby_podcasts.jpg",
    },
    {
        "name": "Trying New Foods",
        "description": "Exploring different cuisines and flavors is one of my favorite things to do.",
        "image": "hobby_food.jpg",
    },
    {
        "name": "Building Projects & Learning New Skills",
        "description": "I enjoy building new projects and constantly picking up new skills to grow as a developer.",
        "image": "hobby_coding.jpg",
    },
]

locations = [
    {"name": "New Zealand", "lat": -40.9006, "lng": 174.886, "note": "An amazing adventure"},
    {"name": "South Africa", "lat": -30.5595, "lng": 22.9375, "note": "Saw the famous safari!"},
    {"name": "Chicago, USA", "lat": 41.8781, "lng": -87.6298, "note": "Best place I have visited so far"},
    {"name": "Lapland, Finland", "lat": 68.0, "lng": 26.0, "note": "Dream destination — I really want to see the northern lights!"},
]

@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    import re
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    content = request.form.get('content', '')

    if not name or name.strip() == '':
        return jsonify({"error": "Invalid name"}), 400
    if not email or not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return jsonify({"error": "Invalid email"}), 400
    if not content or content.strip() == '':
        return jsonify({"error": "Invalid content"}), 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post/<int:id>', methods=['DELETE'])
def delete_timeline_post(id):
    post = TimelinePost.get_by_id(id)
    post.delete_instance()
    return jsonify({"deleted": id})


@app.route('/')
def index():
    return render_template(
        'index.html',
        title="MLH Fellow - Tiea Hapani",
        url=os.getenv("URL"),
        experiences=experiences,
        education=education,
        hobbies=hobbies,
        locations=locations,
    )


@app.route('/hobbies')
def hobbies_page():
    return render_template('hobbies.html', title="My Hobbies", hobbies=hobbies)


@app.route('/timeline')
def timeline():
    posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    timeline_posts = []
    for post in posts:
        post_dict = model_to_dict(post)
        email_hash = hashlib.md5(post.email.strip().lower().encode()).hexdigest()
        post_dict['email_hash'] = email_hash
        timeline_posts.append(post_dict)
    return render_template('timeline.html', title="Timeline", timeline_posts=timeline_posts)
