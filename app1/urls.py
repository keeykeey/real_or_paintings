from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/member<int:member_id>/',views.membersPage,name="memberPage"),
    path('login/member<int:member_id>/contents/',views.contentsPage,name='contentPage')
]

