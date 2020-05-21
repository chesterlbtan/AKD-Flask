import datetime
from flask import render_template, flash, redirect, url_for, request
from typing import List
from webapp import app, db
from webapp.forms import AddSeriesForm, AddRMForm, EditEpisodeForm
from webapp.models import Watchables, Status, Episodes, RunningMan


@app.route('/')
@app.route('/index')
def index():
    jobs = []
    # jobs = [
    #     {'id': 3, 'title': 'MySeries', 'baselink': 'http://localhost:5000', 'status': 'pending', 'progress': 30,
    #      'episodes': [
    #          {'number': 1, 'status': 'done', 'download_link': 'link1', 'progress': 100},
    #          {'number': 2, 'status': 'new', 'download_link': 'link2', 'progress': 0},
    #          {'number': 3, 'status': 'new', 'download_link': 'link3', 'progress': 0},
    #          {'number': 4, 'status': 'new', 'download_link': 'link4', 'progress': 0},
    #          {'number': 5, 'status': 'new', 'download_link': 'link5', 'progress': 0},
    #          {'number': 6, 'status': 'new', 'download_link': 'link6', 'progress': 0},
    #          {'number': 7, 'status': 'new', 'download_link': 'bwahahaha', 'progress': 0},
    #          {'number': 8, 'status': 'new', 'download_link': 'siqmodf', 'progress': 0}
    #      ]},
    #     {'id': 2, 'title': 'MySeries2', 'baselink': 'http://localhost:5000', 'status': 'new', 'progress': 50,
    #      'episodes': [
    #          {'number': 1, 'status': 'new', 'download_link': 'link1', 'progress': 0},
    #          {'number': 2, 'status': 'new', 'download_link': 'link2', 'progress': 0},
    #          {'number': 3, 'status': 'new', 'download_link': 'link3', 'progress': 0},
    #          {'number': 4, 'status': 'new', 'download_link': 'link4', 'progress': 0},
    #          {'number': 5, 'status': 'new', 'download_link': 'link5', 'progress': 0},
    #          {'number': 6, 'status': 'new', 'download_link': 'link6', 'progress': 0}
    #      ]}
    # ]
    sqw: List[Watchables] = Watchables.query.all()
    real_job = []
    for wj in sqw:
        item_stat = Status.query.filter_by(id=wj.id).filter(Status.status != 'moved').first()
        if item_stat is None:
            continue
        ep_stat: List[Episodes] = Episodes.query.filter_by(id=wj.id).all()
        epi_array = []
        for epi in ep_stat:
            ep_item = {'number': epi.episode, 'status': epi.status, 'download_link': epi.lastupdate, 'progress': epi.progress}
            epi_array.append(ep_item)
        epi_array.sort(key=lambda k: k['number'])
        item = {'id': wj.id, 'title': wj.title, 'baselink': wj.baselink, 'status': item_stat.status, 'progress': item_stat.progress,
                'episodes': epi_array}
        real_job.append(item)
    jobs.extend(real_job)
    return render_template('index.html', title='Home', jobs=jobs, showedit=False)


@app.route('/archive')
def archive():
    jobs = []
    sqw: List[Watchables] = Watchables.query.all()
    real_job = []
    for wj in sqw:
        item_stat = Status.query.filter_by(id=wj.id).first()
        ep_stat: List[Episodes] = Episodes.query.filter_by(id=wj.id).all()
        epi_array = []
        for epi in ep_stat:
            ep_item = {'epid': epi.episodes_id, 'number': epi.episode, 'status': epi.status,
                       'download_link': epi.lastupdate, 'progress': epi.progress}
            epi_array.append(ep_item)
        epi_array.sort(key=lambda k: k['number'])
        item = {'id': wj.id, 'title': wj.title, 'baselink': wj.baselink, 'status': item_stat.status,
                'progress': item_stat.progress, 'episodes': epi_array}
        real_job.append(item)
    jobs.extend(real_job)
    return render_template('index.html', title='Archive', jobs=jobs, showedit=True)


@app.route('/adminedit', methods=['GET', 'POST'])
def adminedit():
    if request.args.get('epid'):
        epid = request.args.get('epid')
        ep_item: Episodes = Episodes.query.filter_by(episodes_id=epid).first()
        ep_parent = Watchables.query.filter_by(id=ep_item.id).first()

        editform = EditEpisodeForm()
        if editform.validate_on_submit():
            new_status = editform.status.data
            new_link = editform.dl_link.data
            db.session.query(Episodes).filter(Episodes.episodes_id == epid).\
                update({Episodes.status: new_status, Episodes.base_link: new_link},
                       synchronize_session=False)
            db.session.commit()
            flash(f'Successfully updated <{epid}> status to [{new_status}]')
        else:
            editform.dl_link.data = ep_item.base_link

        job = {'title': ep_parent.title,
               'episode': ep_item.episode,
               'status': ep_item.status,
               'link': ep_item.base_link}
    elif request.args.get('showid'):
        id = request.args.get('showid')
        ep_item: Watchables = Watchables.query.filter_by(id=id).first()
        ep_stat: Status = Status.query.filter_by(id=id).first()

        editform = EditEpisodeForm()
        if editform.validate_on_submit():
            new_status = editform.status.data
            new_link = editform.dl_link.data
            db.session.query(Watchables).filter(Watchables.id == id).\
                update({Watchables.baselink: new_link},
                       synchronize_session=False)
            db.session.query(Status).filter(Status.id == id).\
                update({Status.status: new_status},
                       synchronize_session=False)
            db.session.commit()
            flash(f'Successfully updated <{id}> link')
        else:
            editform.dl_link.data = ep_item.baselink

        job = {'title': ep_item.title, 'episode': -1, 'status': ep_stat.status, 'link': ep_item.baselink}
    return render_template('adminedit.html', title='Admin-Edit', job=job, form=editform)


@app.route('/add', methods=['GET', 'POST'])
def addseries():
    form = AddSeriesForm()
    if form.validate_on_submit():
        item = Watchables()
        item.title = form.title.data
        item.year = form.year.data
        item.episodes = 0
        item.baselink = form.link.data
        item.datetimeadded = datetime.datetime.now()
        item.lastupdate = datetime.datetime.now()
        db.session.add(item)
        db.session.commit()
        item_status = Status(id=item.id, status='new', progress=0.0, location='', remarks='',
                             lastupdate=datetime.datetime.today())
        db.session.add(item_status)
        db.session.commit()

        flash(f'Successfully added <{item.id}> [{form.year.data}] - {form.title.data}, {form.link.data}')
        return redirect(url_for('index'))
    return render_template('addseries.html', title='Add New Series', form=form)


@app.route('/runningman')
def rm():
    jobs = []
    sqw = RunningMan.query.all()
    for wj in sqw:
        item = {'id': wj.rid, 'episode': wj.episode, 'status': wj.status, 'progress': wj.progress,
                'lastupdate': wj.lastupdate}
        jobs.append(item)
    jobs.sort(key=lambda k: k['episode'])
    return render_template('rm.html', title='Running Man', jobs=jobs)


@app.route('/runningman/add', methods=['GET', 'POST'])
def addrm():
    form = AddRMForm()
    if form.validate_on_submit():
        item = RunningMan()
        item.episode = form.episode.data
        item.base_link = form.link.data
        item.status = 'new'
        item.datetimeadded = datetime.datetime.now()
        item.lastupdate = datetime.datetime.now()
        db.session.add(item)
        db.session.commit()

        flash(f'Successfully added <{item.rid}> RunningMan Ep{item.episode}')
        return redirect(url_for('rm'))
    return render_template('addrm.html', title='Queue Running Man Episodes', form=form)
