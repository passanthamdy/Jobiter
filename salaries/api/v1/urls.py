from django.urls import path
from . import views
from .views import salaries_list, salary_delete, salary_create, SalaryUpdate, salary_view

app_name = "salary"

urlpatterns = [
    path('list/', salaries_list, name='list'),
    path('create/', salary_create, name='create'),
    path('view/<int:pk>', salary_view, name='create'),
    path('<int:pk>/delete/', salary_delete, name='delete'),
    path('update/<int:pk>', SalaryUpdate.as_view(), name='generic-update'),

]