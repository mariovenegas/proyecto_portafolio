from django.urls import path, include
from . import views

app_name = 'services'

urlpatterns = [

path('getservices/', views.getservices, name="getservices"),

]