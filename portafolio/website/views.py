from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "website/index.html")

def english(request):
    return render(request, "website/english.html")

def czech(request):
    return render(request, "website/czech.html")