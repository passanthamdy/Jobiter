from django.urls import path
from . import views

app_name = "skills"

urlpatterns = [
    path('', views.HandleAllSkills.as_view()),
    path('<int:pk>', views.HandleEmployeeSkills.as_view()),
]
