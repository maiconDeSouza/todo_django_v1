from django.shortcuts import render, redirect
from django.views import View

from .models import Todo
from .forms import TodoForm


class TodosView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, 'index.html', {'todos': todos})

    def post(self, request):
        todo = TodoForm(request.POST)

        if todo.is_valid():
            todo.save()

        return redirect('home')


class DelView(View):
    def get(self, request, pk):
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect('home')


class UpView(View):
    def get(self, request, pk):
        todos = Todo.objects.all()
        todo = todos.get(id=pk)

        return render(request, 'index.html', {'todos': todos, 'todo': todo})

    def post(self, request, pk):
        new_todo = TodoForm(request.POST)
        if new_todo.is_valid():
            todo = Todo.objects.get(id=pk)
            todo.title = request.POST.get('title')
            todo.save()

        return redirect('home')


class CompletedView(View):
    def get(self, request, pk):
        todo = Todo.objects.get(id=pk)
        todo.completed = not todo.completed
        todo.save()
        return redirect('home')
