from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    text='''<h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Белоусов А.И.</i>
            '''
    return HttpResponse(text)

def Home.as_view()