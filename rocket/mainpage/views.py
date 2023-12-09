from .models import Task
from django.shortcuts import render
import rocket
from mainpage import views
# Create your views here.


def index(request):
    return render(request, 'mainpage/index.html')

def about(request):
    return render(request, 'mainpage/about.html')

def contact(request):
    return render(request, 'mainpage/contact.html')


def index(request):
    result = ""
    for t in Task.objects.all():
        result += t.description
    kateg = ""    
    return render(
        request,
        "mainpage/index.html",
        {"Задачи": Task.objects.all(), "Категории": kateg} # Kонтекст передаваемых переменных

    )