from django.contrib import admin
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
        list_display=['company','reviewer','cons','pros','employment_status','rating','is_published']
        search_fields = ('company','employment_status')
        list_filter = ('employment_status', 'company')
        fieldsets=(
        ('Review Info',{'fields':['company','reviewer','employment_status',]}),
        ('Rating Info',{'fields':['rating',]}),
        ('Extra Info',{'fields':['pros','cons','is_published',]}),
    )
