import time
from referal_system.celery import app


@app.task(bind=True)
def send_sms_task(self, phone_number, confirmation_code):
    time.sleep(2)
