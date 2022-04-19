from datetime import datetime
from settings import db


class AdvModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(64), index=True, unique=True)
    owner = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    date_created = db.Column(db.DateTime(), default=datetime.today().strftime('%Y-%m-%d'))
