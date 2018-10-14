# it will say if you have reached here display views.py to user

from django.conf.urls import url
from . import views

# this (.) says display relative view i.e. importing it to current package

urlpatterns=[
    url('',views.index,name='index')
]
