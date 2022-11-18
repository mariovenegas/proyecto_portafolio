from django.urls import path, include
from . import views

app_name = 'capacitations'

urlpatterns = [

    path('', views.capacitations, name="capacitations"),
    path('create/', views.create, name="create"),
    path('edit/<int:capacitation_id>/', views.edit, name='edit'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:capacitation_id>/', views.update, name='update'),
    path('delete/<int:capacitation_id>/', views.delete, name='delete'),
    path('delete_capacitations/<int:capacitation_id>/', views.delete_capacitations, name='delete_capacitations'),
    path('setstate/', views.setstate, name="setstate"),
    path('capacitation_review/', views.capacitation_review, name='capacitation_review'),
]