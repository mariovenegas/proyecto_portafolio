from django.urls import path, include
from . import views

app_name = 'improvements'

urlpatterns = [

    path('', views.improvements, name="improvements"),
    path('create/', views.create, name="create"),
    path('edit/<int:improvement_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:improvement_id>/', views.update, name='update'),
    path('delete/<int:improvement_id>/', views.delete, name='delete'),
    path('delete_improvements/<int:improvement_id>/', views.delete_improvements, name='delete_improvements'),

]