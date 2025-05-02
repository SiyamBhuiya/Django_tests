from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def siyam(request):
    return HttpResponse("Hello, Siyam!")
def another(request):
    return HttpResponse("Show another route")

def greet(request,name):
    return HttpResponse(f"hello, {name.capitalize()}")