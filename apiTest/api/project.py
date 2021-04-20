#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
# @Time    : 2020/9/10 20:35
# @Author  : Mango
# @File    : Project.py
'''
from apiTest.models import Project
from rest_framework.views import APIView
from apiTest.serializers import ProjectSerializer,ProjectDeserializer
from rest_framework.response import Response
from rest_framework import status

class ProjectList(APIView):
    """
    get:
        返回所有项目信息
    post:
        添加一个新的项目
    """
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProjectDeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
    """
    get:
        返回一个项目实例
    put:
        修改一个项目实例
    delete:
        删除一个项目实例
    """
    def get(self, request, pk, format=None):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProjectSerializer(project)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ProjectSerializer(project, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            project = Project.objects.get(id=pk)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


