from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def siyam(request):
    return HttpResponse("Hello, Siyam!")
def another(request):
    return HttpResponse("Show another route")

def greet(request,name):
    return render(request,"hello/greet.html", {"name": name.capitalize()})