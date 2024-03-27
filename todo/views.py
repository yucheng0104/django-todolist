from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.


def create_todo(request):
    # GET
    message = ""
    form = TodoForm()
    # post
    if request.method == "POST":
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect("todolist")
        except Exception as e:
            print(e)
            message = "建立事項失敗"

    return render(request, 'todo/create-todo.html', {'form': form, "message": message})


def todolist(request):
    # all get filter
    # todos = Todo.objects.all()
    # print(todos)
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)

    # for todo in todos:
    #     print(todo.title)
    return render(request, 'todo/todo.html', {"todos": todos})


def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)

    return render(request, 'todo/view-todo.html', {"todo": todo})
