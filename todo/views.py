from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def delete_todo(request, id):
    # all get filter
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except Exception as e:
        print(e)
    return redirect('todolist')


@login_required
def completed_todo(request):
    todos = None
    completed = True
    if request.user.is_authenticated:
        todos = Todo.objects.filter(
            user=request.user, completed=True).order_by("-created")

    return render(request, 'todo/todo.html', {"todos": todos, "completed": completed})


@login_required
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
        todos = Todo.objects.filter(user=request.user).order_by("-created")

    # for todo in todos:
    #     print(todo.title)
    return render(request, 'todo/todo.html', {"todos": todos})


@login_required
def view_todo(request, id):
    todo = None
    message = ''
    try:
        todo = Todo.objects.get(id=id)
        form = TodoForm(instance=todo)

        if request.method == "POST":
            print(request.POST)

            if request.POST.get("update"):
                todo.date_completed = (
                    datetime.now() if request.POST.get('completed') else None)
                # if request.POST.get("completed"):
                #     todo.date_completed = datetime.now()
                # else:
                #     todo.date_completed = None
                form = TodoForm(request.POST, instance=todo)

                if form.is_valid():
                    form.save()
                    message = '修改成功'

            elif request.POST.get("delete"):
                todo.delete()
                return redirect('todolist')

    except Exception as e:
        print(e)
        message = "修改或刪除失敗...."

    return render(request, 'todo/view-todo.html', {"todo": todo, 'form': form, 'message': message})
