from django.urls import path, include
from . import views

app_name = 'contracts'

urlpatterns = [

    path('', views.contracts, name="contracts"),
    path('create/', views.create, name="create"),
    path('edit/<int:contract_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:contract_id>/', views.update, name='update'),
    path('delete/<int:contract_id>/', views.delete, name='delete'),
    path('delete_contracts/<int:contract_id>/', views.delete_contracts, name='delete_contracts'),
    path('getcontracts/', views.getcontracts, name="getcontracts"),

]