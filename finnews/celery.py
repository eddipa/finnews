import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finnews.settings")

app = Celery("finnews")
app.config_from_object("django.conf:settings", namespace = "CELERY")
app.autodiscover_tasks()
