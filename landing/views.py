#-*- coding: cp1251-*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models.models import *

""" Функция контролирует все запросы к сайту и выводит на него нужную информацию """
def view(request, city):
    if city == "store":
        return render_to_response('store.html')
    else:
        return render_to_response('index.html')


def get_header(option):
    # Функция делает выборку по алиасу и возращает текущий заголовок
    try:
        current_header = headers.objects.get(alias = option)
    except:
        pass
    return current_header


