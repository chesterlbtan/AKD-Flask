from flask import render_template
from webapp import app


@app.route('/')
@app.route('/index')
def index():
    jobs = [
        {'title': 'MySeries', 'baselink': 'http://localhost:5000', 'status': 'pending',
         'episodes': [
             {'number': 1, 'status': 'new', 'download_link': 'link1', 'progress': 0},
             {'number': 2, 'status': 'new', 'download_link': 'link2', 'progress': 0},
             {'number': 3, 'status': 'new', 'download_link': 'link3', 'progress': 0},
             {'number': 4, 'status': 'new', 'download_link': 'link4', 'progress': 0},
             {'number': 5, 'status': 'new', 'download_link': 'link5', 'progress': 0},
             {'number': 6, 'status': 'new', 'download_link': 'link6', 'progress': 0}
         ]},
        {'title': 'MySeries2', 'baselink': 'http://localhost:5000', 'status': 'new',
         'episodes': [
             {'number': 1, 'status': 'new', 'download_link': 'link1', 'progress': 0},
             {'number': 2, 'status': 'new', 'download_link': 'link2', 'progress': 0},
             {'number': 3, 'status': 'new', 'download_link': 'link3', 'progress': 0},
             {'number': 4, 'status': 'new', 'download_link': 'link4', 'progress': 0},
             {'number': 5, 'status': 'new', 'download_link': 'link5', 'progress': 0},
             {'number': 6, 'status': 'new', 'download_link': 'link6', 'progress': 0}
         ]}
    ]
    return render_template('index.html', title='Home', jobs=jobs)
