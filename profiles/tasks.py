from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_request_access_mail(subject, msg, receivers):
    print('inside email')
    send_mail(subject=subject, message=msg, from_email='youssef.15404@gmail.com', recipient_list=receivers)

