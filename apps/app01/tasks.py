from celery.task import periodic_task

from Xingkong.celery import app

from celery import task,shared_task

@app.task()
def add(a, b):
    return a + b

@task
def muti(a, b):
    return a*b