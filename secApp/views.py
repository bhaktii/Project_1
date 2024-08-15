from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pg(request):
    return HttpResponse('This pg have the worst food')
