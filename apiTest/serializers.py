#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/9/10 15:50
# @Author  : Mango
# @File    : serializers.py
'''
from rest_framework import serializers
from apiTest.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    项目信息序列化
    """
    description = serializers.CharField(required=False, allow_blank=True)
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    lastUpdateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    createUserName = serializers.CharField(required=False, source="createUser.username")

    class Meta:
        model = Project
        fields = ("id", "name", "version", "type", "status", "description",
                    "createTime", "lastUpdateTime", "createUser", "createUserName")

class ProjectDeserializer(serializers.ModelSerializer):
    """
    项目信息反序列化
    """
    class Meta:
        model = Project
        fields = ("id", "name", "version", "type", "status", "description",
                    "createTime", "lastUpdateTime", "createUser")