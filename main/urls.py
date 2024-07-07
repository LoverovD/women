from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cat/<slug:cat_slug>/', views.category, name='category'),
]
