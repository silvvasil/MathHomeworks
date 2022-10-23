from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),  
    path('tasks', views.all_tasks, name="all-tasks"),
    path('add_work/<task_id>', views.add_work, name="add-work"),
    path('add_task', views.add_task, name="add-task"),	
    path('show_works', views.show_works, name='show-works'),
	path('delete_work/<work_id>', views.delete_work, name='delete-work'),
	path('update_work/<work_id>', views.update_work, name='update-work'),
	path('delete_task/<task_id>', views.delete_task, name='delete-task'),
	path('update_task/<task_id>', views.update_task, name='update-task'),		
]
