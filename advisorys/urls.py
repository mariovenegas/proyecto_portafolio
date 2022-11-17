from django.urls import path, include
from . import views

app_name = 'advisorys'

urlpatterns = [

    path('', views.advisorys, name="advisorys"),
    path('create/', views.create, name="create"),
    path('edit/<int:advisory_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:advisory_id>/', views.update, name='update'),
    path('delete/<int:advisory_id>/', views.delete, name='delete'),
    path('delete_advisorys/<int:advisory_id>/', views.delete_advisorys, name='delete_advisorys'),
    path('setstate/', views.setstate, name="setstate"),

]