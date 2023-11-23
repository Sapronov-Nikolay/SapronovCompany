from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>OPIAT DVOIKA</h1><h2>%s</h2>' % str((
        request.method, request.META
        )))
    return HttpResponse('<pre>%s</pre>' % request.method)

def page(*a, **b):
    return HttpResponse('<h1>privet</h1>')