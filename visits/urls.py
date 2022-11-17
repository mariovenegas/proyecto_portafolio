from django.urls import path, include
from . import views

app_name = 'visits'

urlpatterns = [

    path('', views.visits, name="visits"),
    path('create/', views.create, name="create"),
    path('edit/<int:visit_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:visit_id>/', views.update, name='update'),
    path('delete/<int:visit_id>/', views.delete, name='delete'),
    path('delete_visits/<int:visit_id>/', views.delete_visits, name='delete_visits'),
    path('setstate/', views.setstate, name="setstate"),

]