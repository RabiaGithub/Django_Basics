from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#this page will say what to return onto as an httpresponse


def index(request):
    return HttpResponse('<h1> This is a TechieNest webpage </h1>')



