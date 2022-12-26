from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse('enjoy pandago')

# Create your views here.
