from django.http import HttpResponse
from django.shortcuts import render
from django.utils import html
from .mselenium import get_something_from_selenium
from .mysqlutil import get_movies_info_from_db


def hello(request):
    context = {}
    context['a1'] = 'Hello World again!'
    context['p1'] = '菜鸟教程yyds'
    # context['p2'] = get_something_from_selenium()
    return render(request, 'runoob.html', context)


def runoob(request):
    return HttpResponse("Hello world ! ")


def movie(request):
    context = {}
    # context['a1'] = 'Hello World again!'
    # context['p1'] = '豆瓣top电影信息：'
    # all_info = html.format_html(get_movies_info_from_db())
    context['info'] = get_movies_info_from_db()
    return render(request, 'movie.html', context)
