from django.urls import path
from . import views
from .views import experiences_list, experience_create

app_name = "experience"

urlpatterns = [
    path('<int:id>/list/', experiences_list, name='list'),
    path('<int:id>/create/', experience_create, name='create'),

]
