from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed,pre_save
from .models import AppliedEmployees, Job
from profiles.models import Employee
from django.core.mail import send_mail
from celery import shared_task
from profiles.models import City
from notifications.models import Notification


@shared_task
@receiver(post_save, sender=Job)
def send_mails_to_matched_users(sender, instance:Job, **kwargs):
    
        # send email logic
    
    title=instance.job_title
    print('title>>>>>',instance)
    users = Employee.objects.filter(job_title=title)
    print(users)
    users_emails = []
    for user in users:
        if user.allow_notification == True:
            users_emails.append(user.email)
            Notification.objects.create(
                user=user, message="Hello job seekers , a job that matches your job title is found, you will find the job in your notification bar",
                job=instance,company=instance.company
            )
    
    users_emails = list(set(users_emails))
    print(users_emails)
    subject="Job Matching"
    msg="Hello job seekers , a job that matches your job title is found, you will find the job in your notification bar"
    send_mail(subject=subject,
        message=msg,
        from_email='youssef.15404@gmail.com',
        recipient_list=users_emails)
   



@receiver(pre_save, sender=AppliedEmployees)
def on_change(sender, instance: AppliedEmployees, **kwargs):
    if instance.id is None: # new object will be created
        pass 
    else:
        previous = AppliedEmployees.objects.get(id=instance.id)
        if previous.accepted != instance.accepted and user.allow_notification == True: # field will be updated
            subject="Job notify"
            user_email=previous.employee.email
            print(user_email)
            msg="You have been choosen to join the interview process with the job you applied for"
            send_mail(subject=subject,
            message=msg,
            from_email='youssef.15404@gmail.com',
            recipient_list=[user_email])
            user=previous.employee
            
            notification=Notification.objects.create(
                    user=user, message="You are accepted to start the interviewing proccess, the company will contact with you to schedule an interview appointment as soon as possible ",job=previous.job,company=previous.job.company
                )
            print('>>>>',notification)