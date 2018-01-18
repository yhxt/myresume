# -*- coding: utf-8 -*-

from django.shortcuts import render


def myresume(request):
    return render(request,'myresume.html')