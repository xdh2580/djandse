from django.http import HttpResponse
from django.shortcuts import render
from .mselenium import get_something_from_selenium


# def runoob(request):
#     views_name = "菜鸟教程"
#     return render(request, "runoob.html", {"p1": views_name})

#add something

def hello(request):
    context = {}
    context['a1'] = 'Hello World again!'
    context['p1'] = '菜鸟教程yyds'
    context['p2'] = get_something_from_selenium()
    return render(request, 'runoob.html', context)


def runoob(request):
    return HttpResponse("Hello world ! ")
