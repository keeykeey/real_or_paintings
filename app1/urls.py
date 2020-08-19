from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/member/',views.membersPage,name="memberPage"),
    path('login/member/content/',views.contentPage,name='contentPage')
]

