from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Category, Women

# Create your views here.
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.published.all()
    data = {
        "menu": menu,
        "title": "Главная страница",
        "posts": posts,
        "cat_selected": 0,
    }
    return render(request, 'main/index.html', context=data)


def about(request):
    data = {
        "menu": menu,
        "title": "О нас",
    }
    return render(request, 'main/about.html', context=data)


def addpage(request):
    return HttpResponse("Добавить статью")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        "menu": menu,
        "post": post,
        "title": post.title,
        "cat_selected": post.cat_id,
    }
    return render(request, 'main/post.html', context=data)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=cat.pk)
    data = {
        "menu": menu,
        "title": cat.name,
        "posts": posts,
        "cat_selected": cat.pk,
    }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
