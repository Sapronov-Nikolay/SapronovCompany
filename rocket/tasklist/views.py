from django.shortcuts import render
from mainpage.models import Task



def task_home(request):
    header = "Личная информация"  # Обычная переменная
    langs = ["Python", "html", "css", "javascript"]  # Массив ["x", "x", №, №]
    user = {"name": "Николай, ", "age": 38}  # Словарь {"x": "x", "x": №}
    addr = ("Городецкая", 8, 1, 137)  # Кортеж ("x", "x", №)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, 'tasklist/task_home.html', context=data)
def task_home(request):
    tasklist = Task.objects.order_by('nachalo')
    return render(request, 'tasklist/task_home.html', {'tasklist':tasklist})