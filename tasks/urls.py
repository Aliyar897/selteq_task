# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    path('tasks/list/', views.get_tasks, name='get_tasks'),
    path('tasks/<int:task_id>/', views.retrieve_task, name='retrieve_task'),
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
