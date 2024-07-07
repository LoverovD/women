from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def category(request, cat_slug):
    return render()


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
