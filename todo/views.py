from django.shortcuts import render
from .models import Todo

# Create your views here.


def todo(request):
    # all get filter
    # todos = Todo.objects.all()
    # print(todos)
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    # for todo in todos:
    #     print(todo.title)
    return render(request, 'todo/todo.html', {"todos": todos})
