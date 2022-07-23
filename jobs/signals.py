from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed,pre_save
from .models import AppliedEmployees, Job
from profiles.models import Employee
from django.core.mail import send_mail
from celery import shared_task
from profiles.models import City



@shared_task
@receiver(m2m_changed, sender=Job.skills.through)
def send_mails_to_matched_users(sender, instance, action, **kwargs):
    if action == 'post_add':
        # send email logic
        skills = instance.skills.all()
        users = Employee.objects.filter(skills__in=skills)
        users_emails = []
        for user in users:
            users_emails.append(user.email)
        users_emails = list(set(users_emails))
        print(users_emails)
        subject="Job Matching"
        msg="Hello job seekers , this job matches your tags, you can apply"
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
        if previous.accepted != instance.accepted: # field will be updated
            subject="Job notify"
            user_email=previous.employee.email
            print(user_email)
            msg="You have been<h1> chosen </h1>to join the interview process with the job you applied for"
            send_mail(subject=subject,
            message=msg,
            from_email='youssef.15404@gmail.com',
            recipient_list=[user_email])