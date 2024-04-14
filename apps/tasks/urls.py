from django.urls import path
from .views import (task_list, 
                    task_view, 
                    new_task, 
                    edit_task, 
                    delete_task)


urlpatterns = [
    path('', task_list, name='task-list'),
    path('task/<int:id>', task_view, name='task-view'),
    path('newtask/', new_task, name='new-task'),
    path('edit/<int:id>', edit_task, name='edit-task'),
    path('delete/<int:id>', delete_task, name='delete-task')
]