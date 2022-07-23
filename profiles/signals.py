from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import City

from django.core.mail import send_mail
from celery import shared_task
from .tasks import send_request_access_mail
from celery import Celery


@shared_task
@receiver(post_save, sender=City)
def city_post_save_action(*args, **kwargs):
    print(args)
    print('----------------')
    print(kwargs)
    print('*********************')
    if kwargs.get('created'):
        obj = kwargs.get('instance')
        subject = '<h3>Test job Email</h3> '
        msg = 'Email Test'
        sender = 'youssef.15404@gmail.com'
        receivers = ['youssef.ibrahem.2022@gmail.com']
        # send_mail(subject=subject, message=msg, from_email='youssef.15404@gmail.com', recipient_list=receivers)
        send_request_access_mail(subject, msg, receivers)

        # send_mail_task.delay(subject,msg,sender, receivers)