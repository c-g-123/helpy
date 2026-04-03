from django.urls import path

from core import views


app_name = 'core'


urlpatterns = [
    path('', views.index, name='index'),

    # Authentication

    path('register/', views.register, name='register'),
    path('register/submit/', views.register_submit, name='register_submit'),
    path('login/', views.login, name='login'),
    path('login/submit/', views.login_submit, name='login_submit'),
    path('logout/', views.logout, name='logout'),

    # Planning

    path('agenda/', views.agenda, name='agenda'),

    # Project

    path('project/create/', views.create_project, name='create_project'),
    path('project/create/submit/', views.create_project_submit, name='create_project_submit'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('project/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('projects/', views.projects, name='projects'),

    # Task

    path('task/create/', views.create_task, name='create_task'),
    path('task/create/submit/', views.create_task_submit, name='create_task_submit'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('task/<int:task_id>/edit', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete', views.delete_task, name='delete_task'),

]
