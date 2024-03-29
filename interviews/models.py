from django.db import models
# Create your models here.


class Interview(models.Model):
    employee_id = models.ForeignKey("accounts.User", verbose_name="Developer ID",blank=True,null=True, on_delete=models.SET_NULL,related_name="interview_employee_id")
    company_id = models.ForeignKey("accounts.User", verbose_name="Company ID",blank=True,null=True, on_delete=models.SET_NULL,related_name="interview_company_id")
    job_title=models.CharField( max_length=50)
    description = models.TextField()
    questions = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    answer=models.TextField(blank=True,null=True)
    published=models.BooleanField(default=False)
    
    
    def __str__(self):
        return "Interview no. "+str(self.id)