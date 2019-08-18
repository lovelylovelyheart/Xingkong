import datetime

from celery.task import periodic_task
from redis import StrictRedis

from Xingkong.celery import app

from celery import task,shared_task
redis = StrictRedis(host='172.0.0.1', port=6379, db=0)
@app.task()
def add(a, b):
    return a + b

@task()
def muti(a, b):
    return a*b

@periodic_task(run_every=datetime.timedelta(seconds=30))
def hello():
    return "hello world"