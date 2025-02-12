from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.conf import settings

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

app = Celery("UnaHealthAPI")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.update(
    broker_url="redis://localhost:6379/0",
    result_backend="redis://localhost:6379/0",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
