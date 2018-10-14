from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'personal/home.html')


def contact(request):
    return render(request,'personal/basic.html', {'content' : ['Feel free for any queries or suggestions, email us on ','query@techienest.in']})
 #adding optional dictionary
