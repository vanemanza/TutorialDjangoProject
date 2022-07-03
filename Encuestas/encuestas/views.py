from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hola Django, ya te tengo!')