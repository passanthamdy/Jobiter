from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('<int:pk>/show/', views.RetrieveUpdateProfile.as_view()),
    path('<int:pk>/update/', views.RetrieveUpdateProfile.as_view()),

]