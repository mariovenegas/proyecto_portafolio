from django.urls import path, include
from . import views

app_name = 'specialadvisorys'

urlpatterns = [

    path('', views.specialadvisorys, name="specialadvisorys"),
    path('create/', views.create, name="create"),
    path('edit/<int:specialadvisorys_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:specialadvisorys_id>/', views.update, name='update'),
    path('delete_specialadvisorys/<int:specialadvisorys_id>/', views.delete_specialadvisorys, name='delete_specialadvisorys'),

]