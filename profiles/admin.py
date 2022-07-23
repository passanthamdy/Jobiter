from django.contrib import admin

from profiles.models import Company, Employee, City
from accounts.admin import UserAdmin


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# Register your models here.
# admin.site.register(Employee)
# admin.site.register(Company)

@admin.register(Employee)
class ChildClassAdmin(UserAdmin):
    list_display = ('id', 'username', 'job_title', 'gender', 'dob', 'cv', 'level', 'city')

    def get_list_display(self, request):
        return self.list_display + ('phone', 'user_type', 'image')

    fieldsets = (
        ('Employee',
         {'fields': ['username', 'password', 'email', 'job_title', 'phone', 'gender', 'image', 'level', 'cv']}),
        ('Personal data section',
         {'fields': ['first_name', 'last_name', 'dob', 'city', 'skills']}),
    )


@admin.register(Company)
class ChildClassAdmin(UserAdmin):
    list_display = (
        'id', 'company_name', 'username', 'address', 'about', 'industry', 'company_size', 'started_at', 'website',
        'city')

    def get_list_display(self, request):
        return self.list_display + ('phone', 'user_type', 'image')

    fieldsets = (
        ('Company', {
            'fields': ['username', 'password', 'company_name', 'industry', 'company_size', 'started_at', 'phone',
                       'image', 'address', 'allow_notification']}),
        ('non required data section',
         {'fields': ['website', 'email', 'city', 'about']}),
    )
