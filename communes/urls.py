from django.urls import path, include
from . import views

app_name = 'communes'

urlpatterns = [

path('getcommunes/', views.getcommunes, name="getcommunes"),

]