from django.urls import path
from . import views

# This is the url use to get the data from the datatable accordingly
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('start/<int:pk>/', views.start_task, name='start_task'),
    path('end/<int:pk>/', views.end_task, name='end_task'),
]
