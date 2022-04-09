from django.shortcuts import render
from .models import InfoImg, Homework, DateNow, Title_odd_week, Title_eveen_week, Border_odd_week, Border_even_week, Desc

def home(request):
    img = InfoImg.objects.all()
    desc = Desc.objects.all()
    return render(request, 'main_page/home.html', {'content': img, 'title': 'Главная', 'desc': desc})

def schedule(request):
    title_even_week = Title_eveen_week.objects.all()
    title_odd_week = Title_odd_week.objects.all()
    border_even_week = Border_even_week.objects.all()
    border_odd_week = Border_odd_week.objects.all()
    return render(request, 'main_page/schedule.html', {'title': 'Расписание', 'title_even_week': title_even_week, 'title_odd_week': title_odd_week, 'border_even_week': border_even_week, 'border_odd_week': border_odd_week})

def abstract(request):
    return render(request, 'main_page/abstract.html', {'title': 'Конспекты'})

def about(request):
    return render(request, 'main_page/about.html', {'title': 'О сайте'})

def homework(request):
    dz = Homework.objects.all()
    dat = DateNow.objects.all()
    return render(request, 'main_page/homework.html', {'title': 'Домашняя работа', 'dz': dz, 'dat': dat})
