from django.shortcuts import render, HttpResponse

# Create your views here.

def about(request):
    return render(request,"ProyectoWebApp/about.html")

def experience(request):
    return render(request,"ProyectoWebApp/experience.html")

def education(request):
    return render(request,"ProyectoWebApp/education.html")

def skills(request):
    return render(request,"ProyectoWebApp/skills.html")

def interests(request):
    return render(request,"ProyectoWebApp/interests.html")

def certifications(request):
    return render(request,"ProyectoWebApp/certifications.html")

def contact(request):
    return render(request,"ProyectoWebApp/contact.html")
