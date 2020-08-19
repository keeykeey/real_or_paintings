from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("start django project right now")

def login(request):
    return HttpResponse('login page')
#    return render(request,'templates/login.html')

def membersPage(request):
    return HttpResponse("This is a member's page")

def contentPage(request):
    return HttpResponse("this is a content page")
