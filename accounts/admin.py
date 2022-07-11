from django.contrib import admin
from .models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type', 'allow_notification', 'phone', 'image')
    search_fields = ('phone', 'user_type')
