import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'referal_system.settings')

app = Celery("django_referal_system", broker_connection_retry_on_startup=False)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
