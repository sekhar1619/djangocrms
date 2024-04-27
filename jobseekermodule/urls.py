from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views
app_name = 'jobseekermodule'
urlpatterns = [
    path('viewjobs/',views.viewjobs,name='viewjobs'),
    path('job_details_list',views.job_details_list,name='job_details_list'),
    path('submit_form/', views.submit_form, name='submit_form'),
    path('addjobseekerprofile/', views.addjobseekerprofile, name='addjobseekerprofile'),
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)