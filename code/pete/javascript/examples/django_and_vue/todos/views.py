from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

import json

from .models import Todo

def index(request):
    return render(request, 'todos/index.html')

def get_todos(request):
    todo_objects = Todo.objects.all()

    todos = []
    for todo_object in todo_objects:
        todo = {
            'id': todo_object.id,
            'description': todo_object.description,
            'completed': todo_object.completed,
        }
        todos.append(todo)

    data = {
        'todos': todos
    }
    return JsonResponse(data)


def add_todo(request):
    if request.method =='POST':
        data = json.loads(request.body)
        Todo.objects.create(description=data.get('description'))
    return HttpResponse('alright!')