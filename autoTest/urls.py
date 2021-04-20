"""autoTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apiTest import views
from django.conf.urls import url
from apiTest import urls as apiUrls
from django.views.generic.base import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPIRenderer

schema_view = get_schema_view("接口管理文档",renderer_classes=[SwaggerUIRenderer,OpenAPIRenderer])

urlpatterns = [
    url('^$', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('test/', views.test),
    url('^api/', include(apiUrls)),
    path('docs/', schema_view)
]
