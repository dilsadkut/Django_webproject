# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name ='index'),
    path('userLogin/',views.userLogin, name ='userLogin'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard/addrecord/', views.addrecord, name='addrecord'),
   
    ]

