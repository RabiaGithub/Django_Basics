#it will say if you have reached here display the views.py file

from django.conf.urls import url
from . import views                #. is relative view saying importing it from current package


urlpatterns=[
    url('',views.index,name='index'),
    url('',views.hello,name='hello'),
]
