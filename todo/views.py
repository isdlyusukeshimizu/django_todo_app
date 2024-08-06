# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# ToDoアイテムのリストを取得
@login_required
def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# ToDoアイテムを追加
@login_required
def add_todo(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm()
    return render(request, 'todo/add_todo.html', {'form': form})

# 既存のToDoアイテムを編集
@login_required
def edit_todo(request, todo_id):
    todo = ToDoItem.objects.get(pk=todo_id)
    if request.method == 'POST':
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = ToDoForm(instance=todo)
    return render(request, 'todo/edit_todo.html', {'form': form, 'todo_id': todo_id})

# ToDoアイテムを削除
@login_required
def delete_todo(request, todo_id):
    todo = ToDoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')  # 登録後にToDoリストへリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})