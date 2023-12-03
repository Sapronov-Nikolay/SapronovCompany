from django.contrib import admin
from django.urls import path
from mainpage import views
from django.urls import path, include
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mainpage/', include('mainpage.urls')),
]

'''navset = [
    {'url': '/',          'text': 'MAIN',    'active': False},
    {'url': '/dela',      'text': 'Dela',    'active': False},
]'''