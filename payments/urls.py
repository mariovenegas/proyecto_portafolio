from django.urls import path, include
from . import views

app_name = 'payments'

urlpatterns = [

    path('', views.payments, name="payments"),
    path('pay/', views.pay, name="pay"),


]