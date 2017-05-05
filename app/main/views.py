# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from flask import render_template,jsonify
from . import main
from ..models import CPUInfo


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/cpuinfo/<int:day>', methods=['GET'])
def cpuinfo(day):
    second = datetime.utcnow()
    diff = timedelta(minutes=day)
    first = second - diff
    sd = CPUInfo.query.filter(CPUInfo.create_time.between(first, second)).all()
    create_time = []
    cpu_ratio = []
    for value in sd:
        create_time.append(value.create_time)
        cpu_ratio.append(value.cpu_utilization)

    return jsonify(time=create_time, ratio=cpu_ratio), 200
