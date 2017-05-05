# -*- utf-8 -*-
from __future__ import division
import os
import time
from . import db, create_app, create_celery
from .models import CPUInfo


celery = create_celery(create_app(os.getenv('FLASK_CONFIG') or 'default'))

@celery.task
def add(x, y):
    return x+y


def get_cpu_info():
    with open('/proc/stat') as f:
        total_cpu = 0
        line = f.readline()
        string_list = line.strip().split()

        idle = int(string_list[4].strip())

        for value in string_list[1:]:
            total_cpu += int(value.strip())

        return total_cpu - idle, total_cpu


@celery.task(name="get_cpu")
def get_cpu():
    usage_1, total_1= get_cpu_info()
    time.sleep(1)
    usage_2, total_2 = get_cpu_info()
    try:
        cpu_ratio = 100*(usage_2 - usage_1) / (total_2 - total_1)
    except Exception:
        cpu_ratio = 0

    cpu = CPUInfo(cpu_utilization=round(cpu_ratio, 2))
    db.session.add(cpu)
    db.session.commit()



