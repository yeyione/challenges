from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Este es un mensaje desde el index")
def january(request):
    return HttpResponse("Walk fot at least 30 min every day.")
def february(request):
    return HttpResponse("Go to the gym every day")
def march(request):
    return HttpResponse("Eat healthy every day")
