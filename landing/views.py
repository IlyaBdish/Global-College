#-*- coding: cp1251-*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models.models import *

""" ������� ������������ ��� ������� � ����� � ������� �� ���� ������ ���������� """
def view(request, city):
    if city == "store":
        return render_to_response('store.html')
    else:
        return render_to_response('index.html')


def get_header(option):
    # ������� ������ ������� �� ������ � ��������� ������� ���������
    try:
        current_header = headers.objects.get(alias = option)
    except:
        pass
    return current_header


