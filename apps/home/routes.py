# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps.home import blueprint
from flask import render_template, request, Flask
from jinja2 import TemplateNotFound

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/hebrew")
def hebrew():
    return render_template("hebrew.html")

@app.route("/russian")
def russian():
    return render_template("russian.html")

@app.route("/english")
def english():
    return render_template("english.html")

# @blueprint.route('/index')
# def index():
#     return render_template('home/index.html', segment='index')


@blueprint.route('/<template>')
def route_template(template):

    try:
        if not template.endswith('.html'):
            template += '.html'
        # Detect the current page
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
# def get_segment(request):

#     try:
#         segment = request.path.split('/')[-1]
#         if segment == '':
#             segment = 'index'
#         return segment

#     except:
#         return None
