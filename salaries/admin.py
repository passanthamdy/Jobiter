from django.contrib import admin
from .models import Salary
# Register your models here.

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
        list_display=['salary','company','reviewer','job_title','start_date','end_date','is_published']
        search_fields = ('job_title','salary','company')
        list_filter = ('job_title', 'company')
        fieldsets=(
        ('Staff Info',{'fields':['company','reviewer',]}),
        ('Salary Info',{'fields':['job_title','salary',]}),
        ('Date Section',{'fields':['start_date','end_date',]}),
        ('Extra Info',{'fields':['is_published',]}),
    )