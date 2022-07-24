from django.urls import path
from . import views
from .views import salaries_list, salary_create, salary_view

app_name = "salary"

urlpatterns = [
    path('<int:id>/list/', salaries_list, name='list'),
    path('<int:id>/create/', salary_create, name='create'),
    path('view/<int:pk>', salary_view, name='create'),

]