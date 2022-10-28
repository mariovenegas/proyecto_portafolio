from django.urls import path, include
from . import views

app_name = 'reportaccidents'

urlpatterns = [

    path('', views.reportaccidents, name="reportaccidents"),
    path('create/', views.create, name="create"),
    path('edit/<int:reportaccident_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:reportaccident_id>/', views.update, name='update'),
    path('delete/<int:reportaccident_id>/', views.delete, name='delete'),
    path('delete_reportaccident/<int:reportaccident_id>/', views.delete_reportaccident, name='delete_reportaccident'),

]