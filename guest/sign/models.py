# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=100)
    limit=models.IntegerField()
    status=models.BooleanField()
    address=models.CharField(max_length=200)
    strart_time=models.DateTimeField('event time')
    create_time=models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

#嘉宾表
class Guest(models.Model):
    event=models.ForeignKey(Event)#关联发布会id
    realname=models.CharField(max_length=64)
    phone=models.CharField(max_length=16)
    email = models.EmailField()
    sign=models.BooleanField()
    create_time=models.DateTimeField(auto_now=True)

class Meta:
    unique_together=("event","phone")

def _str_(self):
    return self.realname
