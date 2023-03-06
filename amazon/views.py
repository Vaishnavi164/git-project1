from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sannu(request):
    return HttpResponse('<h1> sannu is best frd in my life</h1>')

def vasantha(request):
    return HttpResponse('<h1> vasantha is my chinchan</h1>')    