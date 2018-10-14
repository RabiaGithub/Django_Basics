from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1> Hey... Welcome to TechieNest </h1>')

def hello(request):
    return HttpResponse('<h2> EXPLORING DJANGO !!!! </h2>')
