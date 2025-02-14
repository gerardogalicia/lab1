from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World! This came from the index view')
# Create your views here.

def task_list(request):
    ctx = {
"tasks": [
"task 1",
"task 2",
"task 3",
"task 4",
"task 5",
    ]
}
    return (HttpResponse(render(request, 'task_list.html', ctx,)))