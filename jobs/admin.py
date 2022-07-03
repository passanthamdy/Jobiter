
from .models import Job
from django.contrib import admin

# Register your models here.
# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ['company', 'job_title','level','Description','job_type', 'work_type','salary','state','get_skills',]
#     search_fields = ('company','level','job_title','job_type','work_type')
    
#     def get_skills(self, obj):
#             if obj.skill.all():
#                 return list(obj.skill.all().values_list('name', flat=True))
#             else:
#                 return 'No Skills Yet...'
#     get_skills.short_description = 'Skills'
        