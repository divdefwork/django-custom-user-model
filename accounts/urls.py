""" File description """
# !/usr/bin/env python3
# -*- coding=utf-8 -*-

from django.urls import path

from .views import signup, log_in, log_out

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
]
