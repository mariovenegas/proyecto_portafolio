from django.urls import path, include
from . import views

app_name = 'reports'

urlpatterns = [

    path('', views.reports, name="reports"),

]