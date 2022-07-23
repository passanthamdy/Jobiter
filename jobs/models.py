from datetime import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from skills.models import Skill
from accounts.models import User

JOB_STATUS = (
    ("FULLTIME", "Full-Time"),
    ("PARTTIME", "Part-Time"),
    ("INTERN", "Internship"),

)
LEVEL = (
    ("JUNIOR", "Junior"),
    ("SENIOR", "Senior"),
    ("ENTRY-LEVEL", "Entry-level"),
)
WORK = (
    ("REMOTE", "Remote"),
    ("ONSITE", "Onsite"),
    ("HYBRID", "Hybrid"),
)
STATE = (
    ("OPEN", "Open"),
    ("CLOSED", "Closed"),

)


# Create your models here.
class Job(models.Model):
    company=models.ForeignKey("profiles.Company", verbose_name="Company", on_delete=models.CASCADE)
    job_title=models.CharField( max_length=50)
    level=models.CharField(choices=LEVEL, max_length=50)
    Description=models.TextField()
    job_type=models.CharField(choices=JOB_STATUS, max_length=50)
    work_type=models.CharField(choices=WORK, max_length=50)
    salary = models.IntegerField()
    state=models.CharField(choices=STATE, max_length=50, default='OPEN')
    skills=models.ManyToManyField(Skill, blank=True, null=True)
    created_at=models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return "Job "+ self.job_title

class AppliedEmployees(models.Model):
    job=models.ForeignKey("jobs.Job", verbose_name="Job", on_delete=models.CASCADE)
    employee=models.ForeignKey("profiles.Employee", verbose_name="Employee", on_delete=models.CASCADE)
    cv = models.FileField(upload_to='user_cvs/', null=True, blank=True,
    validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    notice_period=models.IntegerField()
    years_of_exp=models.IntegerField()
    cover_letter=models.TextField()
    accepted=models.BooleanField(default=False)
    created_at=models.DateField(auto_now=False, auto_now_add=True,null=True)

    def __str__(self):
        return self.job.job_title 