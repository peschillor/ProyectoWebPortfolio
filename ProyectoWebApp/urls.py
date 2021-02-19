from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.about, name="ABOUT"),
    path('experience', views.experience, name="EXPERIENCE"),
    path('education', views.education, name="EDUCATION"),
    path('skills', views.skills, name="SKILLS"),
    path('interests', views.interests, name="INTERESTS"),
    path('certifications', views.certifications, name="CERTIFICATIONS"),
   
    ]