from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def longBoat(request):
    return HttpResponse('This pub have the best drinks')

def bhakti(request):
    return HttpResponse('Bhakti is a good girl')
