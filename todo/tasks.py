import datetime

from celery import shared_task
import time

from internship.celery_app import app
from todo.models import TaskItem


@app.task
def create_task():
    TaskItem.objects.create(title="bla", date_due=datetime.datetime.now())
