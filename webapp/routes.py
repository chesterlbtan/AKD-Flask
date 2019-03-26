from flask import render_template
from webapp import app


@app.route('/')
@app.route('/index')
def index():
    jobs = [
        {'id': 1, 'title': 'MySeries', 'baselink': 'http://localhost:5000', 'status': 'pending', 'progress': 30,
         'episodes': [
             {'number': 1, 'status': 'done', 'download_link': 'link1', 'progress': 100},
             {'number': 2, 'status': 'new', 'download_link': 'link2', 'progress': 0},
             {'number': 3, 'status': 'new', 'download_link': 'link3', 'progress': 0},
             {'number': 4, 'status': 'new', 'download_link': 'link4', 'progress': 0},
             {'number': 5, 'status': 'new', 'download_link': 'link5', 'progress': 0},
             {'number': 6, 'status': 'new', 'download_link': 'link6', 'progress': 0},
             {'number': 7, 'status': 'new', 'download_link': 'bwahahaha', 'progress': 0},
             {'number': 8, 'status': 'new', 'download_link': 'siqmodf', 'progress': 0}
         ]},
        {'id': 2, 'title': 'MySeries2', 'baselink': 'http://localhost:5000', 'status': 'new', 'progress': 50,
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
