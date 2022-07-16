from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    #Company urls >> jobs/company/co...
    path('create/', views.ListCompanyJobs.as_view()),
    path('', views.ListCompanyJobs.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDeleteCompanyJob.as_view()),
    #path('<int:pk>/accept/',views.AcceptDeveloper),
    path('<int:pk>/close/',views.close_job),
    path('applied-jobs/',views.list_applied_jobs),
    path('applied_employees', views.list_applied_employees),
    path('<int:pk>/apply/',views.ApplyForJob.as_view()),


]