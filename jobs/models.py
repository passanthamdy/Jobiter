from django.db import models

from skills.models import Skill

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
    company = models.ForeignKey("accounts.User", verbose_name="Company", on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    level = models.CharField(choices=LEVEL, max_length=50)
    Description = models.TextField()
    job_type = models.CharField(choices=JOB_STATUS, max_length=50)
    work_type = models.CharField(choices=WORK, max_length=50)
    salary = models.IntegerField()
    state = models.CharField(choices=STATE, max_length=50)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return "Job no. " + self.id
