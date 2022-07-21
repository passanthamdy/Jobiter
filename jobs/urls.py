from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    #Company urls >> jobs/company/co...
    path('create/', views.CreateJob),
    path('', views.ListCompanyJobs),
    path('<int:pk>/', views.RetrieveUpdateDeleteCompanyJob.as_view()),
    path('<int:pk>/close/',views.close_job),
    path('<int:pk>/applied_employees', views.list_applied_employees),
    path('<int:job_id>/applied_employees/accept_employee/', views.accept_employee),
    path('<int:pk>/applied_employees/view_applicant/', views.view_applicant),

#   employee url >>
    path('applied-jobs/',views.list_applied_jobs),
    path('<int:pk>/apply/',views.ApplyForJob.as_view()),
    path('all_jobs/',views.ListJobs.as_view()),
    




]