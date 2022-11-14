from django.urls import path, include
from . import views

app_name = 'checklists'

urlpatterns = [

    path('', views.checklists, name="checklists"),
    path('create/', views.create, name="create"),
    path('edit/<int:checklist_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:checklist_id>/', views.update, name='update'),
    path('delete/<int:checklist_id>/', views.delete, name='delete'),
    path('delete_checklists/<int:checklist_id>/', views.delete_checklists, name='delete_checklists'),

]