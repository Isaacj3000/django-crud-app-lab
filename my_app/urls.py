from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name='home'),  # Add home as the root URL
    path('register/', views.register, name='register'),  # Add registration URL
    path('login/', views.user_login, name='login'),  # Add custom login URL
    path('logout/', views.user_logout, name='logout'),  # Add custom logout URL
    path('plants/', views.plant_list, name='plant_list'),
    path('plants/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plants/new/', views.plant_create, name='plant_create'),
    path('plants/<int:pk>/edit/', views.plant_edit, name='plant_edit'),
    path('plants/<int:pk>/delete/', views.plant_delete, name='plant_delete'),
    
    # Watering Record URLs
    path('plants/<int:plant_pk>/water/', views.watering_record_create, name='watering_record_create'),
    path('plants/<int:plant_pk>/watering-history/', views.watering_record_list, name='watering_record_list'),
    path('plants/<int:plant_pk>/watering-history/<int:record_pk>/delete/', views.watering_record_delete, name='watering_record_delete'),
    
    path('care-tasks/', views.care_task_list, name='care_task_list'),
    path('care-tasks/<int:pk>/', views.care_task_detail, name='care_task_detail'),
    path('care-tasks/new/', views.care_task_create, name='care_task_create'),
    path('care-tasks/<int:pk>/edit/', views.care_task_edit, name='care_task_edit'),
    path('care-tasks/<int:pk>/delete/', views.care_task_delete, name='care_task_delete'),
    path('care-tasks/<int:pk>/complete/', views.care_task_complete, name='care_task_complete'),
    path('plants/<int:plant_pk>/care-tasks/', views.plant_care_tasks, name='plant_care_tasks'),
] 