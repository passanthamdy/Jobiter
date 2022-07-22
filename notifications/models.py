from django.db import models


# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey("accounts.User", related_name='notification_user', on_delete=models.CASCADE)
    company=models.ForeignKey('profiles.Company',related_name='company', null=True, on_delete=models.SET_NULL, default=None)
    job=models.ForeignKey("jobs.Job", on_delete=models.SET_DEFAULT,null=True, default=None)
    employee=models.ForeignKey('profiles.Employee', related_name='employee',null=True, on_delete=models.SET_DEFAULT, default=None)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message