from django.contrib import admin

from profiles.models import Company, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Company)

