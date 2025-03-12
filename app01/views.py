from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('hello world')

def list(request):
    author = 'eil'
    article_number = 20
    article_list = ['第一章：什么是django','第二章：django的mvt模式',]
    info = {
        'name': 'eil',
        'age': 20,
        'programming': ['python','java']
    }
    return render(request, 'list.html',{
        'author': author,
        'article_number': article_number,
        'article_list': article_list,
        'info': info,
    })
