from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'employermodule'
urlpatterns = [
    path('jobpost/',views.jobpost,name='jobpost'),
    path('add_job_details',views.add_job_details,name='add_job_details'),
    path('view/',views.view_job_details,name='view_job_details'),
    path('edit/<int:job_id>/', views.edit_job_details, name='edit_job_details'),
    path('delete/<int:job_id>/',views.delete_job_details,name='delete_job_details'),
    path('job_application_list/', views.job_application_list, name='job_application_list'),
]