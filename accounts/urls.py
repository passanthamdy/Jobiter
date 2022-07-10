from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import company_signup,employee_signup, user_logout, custom_login
app_name='accounts'


urlpatterns = [
    path('login/', custom_login.as_view()),
    path('user_logout/', user_logout,),
    path('employee_signup/', employee_signup, name='developer_signup'),
    path('company_signup/', company_signup, name='company_signup'),
]