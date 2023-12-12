
from django.shortcuts import render
import rocket
from mainpage import views
# Create your views here.


def index(request):
    header = "Личная информация"  # Обычная переменная
    langs = ["Python", "html", "css", "javascript"]  # Массив ["x", "x", №, №]
    user = {"name": "Николай, ", "age": 38}  # Словарь {"x": "x", "x": №}
    addr = ("Городецкая", 8, 1, 137)  # Кортеж ("x", "x", №)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, 'mainpage/index.html', context=data)

def about(request):
    header = "Личная информация"  # Обычная переменная
    langs = ["Python", "html", "css", "javascript"]  # Массив ["x", "x", №, №]
    user = {"name": "Николай, ", "age": 38}  # Словарь {"x": "x", "x": №}
    addr = ("Городецкая", 8, 1, 137)  # Кортеж ("x", "x", №)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, 'mainpage/about.html', context=data)

def contact(request):
    header = "Личная информация"  # Обычная переменная
    langs = ["Python", "html", "css", "javascript"]  # Массив ["x", "x", №, №]
    user = {"name": "Николай, ", "age": 38}  # Словарь {"x": "x", "x": №}
    addr = ("Городецкая", 8, 1, 137)  # Кортеж ("x", "x", №)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, 'mainpage/contact.html', context=data)
