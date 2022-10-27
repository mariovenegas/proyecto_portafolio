from django.urls import path, include
from . import views

app_name = 'professionals'

urlpatterns = [

    path('', views.professionals, name="professionals"),
    path('create/', views.create, name="create"),
    path('edit/<int:professional_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:professional_id>/', views.update, name='update'),
    path('delete/<int:professional_id>/', views.delete, name='delete'),
    path('delete_professional/<int:professional_id>/', views.delete_professional, name='delete_professional'),

]