# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("hello Django!")
    return render(request,"index.html")
