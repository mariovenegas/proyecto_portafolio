from django.urls import path, include
from . import views

app_name = 'clients'

urlpatterns = [

    path('', views.clients, name="clients"),
    path('create/', views.create, name="create"),
    path('edit/<int:client_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:client_id>/', views.update, name='update'),
    path('delete/<int:client_id>/', views.delete, name='delete'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),

]