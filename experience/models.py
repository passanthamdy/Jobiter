from django.db import models

# Create your models here.
class Experience(models.Model):
    user=models.ForeignKey("accounts.User", verbose_name="Employee", on_delete=models.CASCADE)
    company_name=models.CharField(max_length=150)
    job_title=models.CharField(max_length=150)
    start_date= models.DateField()
    end_date= models.DateField(null=True, default=None)
    description=models.TextField()

    def __str__(self):
        return self.user.username + " "+"Experience in "+self.company_name
    

