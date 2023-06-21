from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    context = {
        'todo': todo
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()
    return redirect('todos:detail', todo.pk)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'detail.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')
    todo.save()
    return redirect('todos:detail', todo.pk)


def completed(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == True:
        todo.completed = False
        todo.save()
    else:
        todo.completed = True
        todo.save()
    return redirect('todos:index')