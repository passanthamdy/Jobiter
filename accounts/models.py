from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser

# # Create your models here.
USER_TYPE = (
    ('EMPLOYEE', 'Employee'),
    ('COMPANY', 'Company'),
)


class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE, max_length=50, default="EMPLOYEE")
    allow_notification = models.BooleanField(default=False)
    phone=models.CharField(max_length=50,)
    image =models.ImageField(upload_to="user_images/")



    



    def __str__(self):
        return self.username + ' ' + self.user_type

    # def __str__(self):
    #     return str('%s %s ' % (self.phone, self.user_type))