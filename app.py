import os
from flask import Flask
from flask import render_template
from flask import request
from celery import Celery

app = Flask(__name__)

celery = Celery(app.name, broker=os.environ['REDIS_URL'])
celery.conf.update(broker_url=os.environ['REDIS_URL'], result_backend=os.environ['REDIS_URL'])

@celery.task
def hello(name):
    return "Hello "+name

@app.route("/")
def root():
    name = request.args.get('name', 'John Doe')
    result = hello.delay(name)
    result.wait()
    return render_template('index.html', celery=result)
