from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Rango says 'Hey there, partner'. <br> <a href='/rango/about/'> About </a>")

def about(request):
    return HttpResponse("Rango says this here is the about page. <br> <a href='/rango/'> Home </a>")