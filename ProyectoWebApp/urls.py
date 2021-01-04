from django.urls import path
from ProyectoWebApp import views



urlpatterns = [
    path('', views.about, name="ABOUT"),
    path('experience', views.experience, name="EXPERIENCE"),
    path('education', views.education, name="EDUCATION"),
    path('skills', views.skills, name="SKILLS"),
    path('interests', views.interests, name="INTERESTS"),
    path('certifications', views.certifications, name="CERTIFICATIONS"),
    path('blog', views.blog, name="BLOG"),
    path('contact', views.contact, name="CONTACTS"),
    
    ]