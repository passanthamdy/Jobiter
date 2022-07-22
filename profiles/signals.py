from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import City

from django.core.mail import send_mail
from celery import shared_task

@shared_task
@receiver(post_save, sender=City)
def city_post_save_action(*args, **kwargs):
    print(args)
    print('----------------')
    print(kwargs)
    print('*********************')
    if kwargs.get('created'):
        obj = kwargs.get('instance')
        subject = 'Test job Email '
        msg = 'Email Test'
        receivers = ['passant.hamdy99@gmail.com', 'youssef.ibrahem.2022@gmail.com']
        send_mail(subject=subject, message=msg, from_email='youssef.15404@gmail.com', recipient_list=receivers)
