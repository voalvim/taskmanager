from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task-list'),
    path('task/new/', views.task_create, name='task-create'),
    path('task/<int:pk>/edit/', views.task_update, name='task-update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),
]
