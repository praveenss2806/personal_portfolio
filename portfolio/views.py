from django.shortcuts import render
from .models import About

# Create your views here.
def home(request):
    abouts=About.objects.all()
    return render(request,"portfolio/home.html",{"abouts":abouts})
