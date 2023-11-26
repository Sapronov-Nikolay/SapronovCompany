from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

def index(request):
    return HttpResponse('<h1>OPIAT DVOIKA</h1><h2>%s</h2>' % str((
        request.method, request.META
        )))
    return HttpResponse('<pre>%s</pre>' % request.method)

def page(*a, **b):
    return HttpResponse('<h1>privet</h1>')


def index(request):
    result = ""
    for t in Task.objects.all():
        result += t.description
    kateg = ""    
    #for a in Kategorii.objects.all():
    #    kateg += a.kategoriya    
    return render(
        request,
        "mainpage/index.html",
        {"Задачи": Task.objects.all(), "Категории": kateg} # Kонтекст передаваемых переменных

    )