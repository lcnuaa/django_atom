# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("hello Django!")
    return render(request,"index.html")
def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='admin' and password=='admin':
            return HttpResponse('login success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})
