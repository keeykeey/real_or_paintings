from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("start django project right now")

def login(request):
    return HttpResponse('login page')
#    return render(request,'templates/login.html')

def membersPage(request,member_id):
    return HttpResponse("This is a member{}'s page".format(member_id))

def contentsPage(request,member_id):
    return HttpResponse("this is a member{}s contents page".format(member_id))
