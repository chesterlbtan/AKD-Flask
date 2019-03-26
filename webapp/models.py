from webapp import db


class Watchables(db.Model):
    __tablename__ = 'watchables'
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.TEXT, nullable=False)
    year = db.Column(db.INTEGER, nullable=False)
    episodes = db.Column(db.INTEGER, nullable=False)
    baselink = db.Column(db.TEXT, nullable=False)
    remarks = db.Column(db.TEXT)
    datetimeadded = db.Column(db.DATE, nullable=False)
    lastupdate = db.Column(db.DATE, nullable=False)

    def __repr__(self):
        return f'<Watchables {self.id}>'

    def __str__(self):
        return f'[{self.year}] - {self.title}'


class Status(db.Model):
    __tablename__ = 'status'
    sid = db.Column(db.INTEGER, primary_key=True)
    id = db.Column(db.INTEGER, db.ForeignKey(Watchables.id), nullable=False)
    status = db.Column(db.TEXT, nullable=False)
    progress = db.Column(db.FLOAT, nullable=False)
    location = db.Column(db.TEXT, nullable=False)
    lastupdate = db.Column(db.DATE, nullable=False)
    remarks = db.Column(db.TEXT)


class Episodes(db.Model):
    __tablename__ = 'episodes'
    episodes_id = db.Column(db.INTEGER, primary_key=True)
    id = db.Column(db.INTEGER, db.ForeignKey(Watchables.id), nullable=False)
    episode = db.Column(db.INTEGER, nullable=False)
    status = db.Column(db.TEXT, nullable=False)
    base_link = db.Column(db.TEXT, nullable=False)
    download_link = db.Column(db.TEXT, nullable=False)
    progress = db.Column(db.FLOAT, nullable=False)
    size = db.Column(db.INTEGER, nullable=False)
    duration = db.Column(db.INTEGER)
    remarks = db.Column(db.TEXT)
    datetimeadded = db.Column(db.DATE, nullable=False)
    lastupdate = db.Column(db.DATE, nullable=False)
    location = db.Column(db.TEXT)
