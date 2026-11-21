from django.urls import path
from . import views

urlpatterns = [
    path('tasks/',views.task_list, name="task_list"),
    path('tasks/<int:pk>',views.task_detail, name="task_detail"),
    path('tasks/new/',views.create_task,name="task_create"),
    path('tasks/<int:pk>/edit/', views.edit_task, name="task_edit"),      
    path('tasks/<int:pk>/delete/', views.delete_task, name="task_delete"),
]