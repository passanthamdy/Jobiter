from django.db import models

# Create your models here.
class Salary(models.Model):
    company=models.ForeignKey("accounts.User", verbose_name="Company", on_delete=models.CASCADE)
    reviewer=models.ForeignKey("accounts.User", verbose_name="Reviewer", on_delete=models.CASCADE)
    salary = models.IntegerField()
    job_title=models.CharField( max_length=50)
    start_date= models.DateField()
    end_date= models.DateField(null=True, default=None)
    is_published= models.BooleanField(default=False)



    def __str__(self):
        return "Salary review no. "+ self.id
    

