from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("Cookbook index page")

def index (page1):
    return HttpResponse("Cookbook page 1")