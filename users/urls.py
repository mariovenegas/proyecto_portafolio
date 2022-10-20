from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [

    path('', views.users, name="users"),
    path('create/', views.create, name="create"),
    path('edit/<int:user_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:user_id>/', views.update, name='update'),
    path('delete/<int:user_id>/', views.delete, name='delete'),

]