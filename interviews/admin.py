from django.contrib import admin
from .models import Interview
# Register your models here.
@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
        list_display=['job_title','company_id','employee_id','description','questions','date','answer',]
        search_fields = ('job_title',)
        list_filter = ('job_title',)
        fieldsets=(
        ('Job Info',{'fields':['job_title','description',]}),
        ('Staff Info',{'fields':['company_id','employee_id',]}),
        ('Extra Info',{'fields':['questions','answer',]}),
    )
