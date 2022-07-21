from django.contrib import admin

from jobs.models import AppliedEmployees, Job

# Register your models here.
admin.site.register(Job)
admin.site.register(AppliedEmployees)