from django.urls import path
from .views import ListNotifications

app_name = 'notification'

urlpatterns = [
    path("list/", ListNotifications.as_view()),
   
]