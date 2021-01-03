from django.shortcuts import render, HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("ABOUT")

def experience(request):
    return HttpResponse("EXPERIENCE")

def education(request):
    return HttpResponse("EDUCATION")

def skills(request):
    return HttpResponse("SKILLS")

def interests(request):
    return HttpResponse("INTERESTS")

def certifications(request):
    return HttpResponse("CERTIFICATIONS")

def blog(request):
    return HttpResponse("BLOG")

def contact(request):
    return HttpResponse("CONTACT")
