from django.shortcuts import render
from django.http import HttpResponse
from apiTest.models import Project

# Create your views here.

def test(request):
    #return HttpResponse("Test!")
    return render(request, "test.html")
