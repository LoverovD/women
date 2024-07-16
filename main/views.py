from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Women

# Create your views here.
menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'addpage'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли',
        'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби',
        'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс',
        'content': 'Биография Джулия Робертс', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
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
        "cat_selected": 0,
    }
    return render(request, 'main/post.html', context=data)


def show_category(request, cat_id):
    data = {
        "menu": menu,
        "title": f"Категория №{cat_id}",
        "posts": data_db,
        "cat_selected": cat_id,
    }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
