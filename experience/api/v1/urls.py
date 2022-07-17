from django.urls import path
from . import views
from .views import experiences_list, experience_delete, experience_create

app_name = "experience"

urlpatterns = [
    path('list/', experiences_list, name='list'),
    path('create/', experience_create, name='create'),
    path('<int:pk>/delete/', experience_delete, name='delete'),

]
