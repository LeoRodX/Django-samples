from django.contrib import admin
from css_app import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.categories),
    path('about/', views.about, name='about'),
    path('quiz/', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
]
