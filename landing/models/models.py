#-*- coding: cp1251-*-
from django.db import models
from django.contrib import admin
""" Таблица хранящая в себе базу людей оставивших заявку """
class buyer(models.Model):
    
    full_name = models.CharField (max_length=20);
    phone_nubmer = models.TextField();
    email = models.CharField (max_length=35)

class headers(models.Model):
    alias = models.CharField (max_length=3);
    title = models.TextField()
    
admin.site.register(headers)