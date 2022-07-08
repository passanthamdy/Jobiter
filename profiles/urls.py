from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('<int:pk>/show/', views.RetrieveUpdateCompany.as_view()),
    path('<int:pk>/update/', views.RetrieveUpdateCompany.as_view()),

]