# -*- coding:utf-8 -*-
from datetime import datetime

from . import db


class CPUInfo(db.Model):
    __tablename__ = 'cpu'
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime(), default=datetime.utcnow)
    cpu_utilization = db.Column(db.Float(precision=4))


