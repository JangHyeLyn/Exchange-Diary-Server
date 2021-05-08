from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add():
    for i in range(10000):
        print(i)