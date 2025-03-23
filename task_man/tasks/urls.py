from django.urls import path
from tasks import views


urlpatterns = [ 
    path('', views.tasks_list, name='tasks_list'),
    path('create/', views.create_task, name='create_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
]
  
  
