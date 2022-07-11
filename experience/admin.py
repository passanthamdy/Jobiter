from django.contrib import admin
from .models import Experience
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'company_name','job_title','description','start_date', 'end_date', ]
    search_fields = ('user','company_name','job_title')
