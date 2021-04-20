#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/9/10 20:44
# @Author  : Mango
# @File    : urls.py
'''
from django.conf.urls import url
from apiTest.api.project import ProjectList,ProjectDetail

urlpatterns = [
    url('projects/$', ProjectList.as_view()),
    url('projects/(?P<pk>[0-9]+)/$', ProjectDetail.as_view())
]
