from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("start django project right now")

def login(request):
#    return HttpResponse('login page')
    return render(request,'templates/login.html')
