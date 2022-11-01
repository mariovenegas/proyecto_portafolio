from django.urls import path, include
from . import views

app_name = 'administrators'

urlpatterns = [

    path('', views.administrators, name="administrators"),
    path('create/', views.create, name="create"),
    path('edit/<int:administrator_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:administrator_id>/', views.update, name='update'),
    path('delete_administrator/<int:administrator_id>/', views.delete_administrator, name='delete_administrator'),

]