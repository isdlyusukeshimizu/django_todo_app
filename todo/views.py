# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoForm

# ToDoアイテムのリストを取得
def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

# ToDoアイテムを追加
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
def delete_todo(request, todo_id):
    todo = ToDoItem.objects.get(pk=todo_id)
    todo.delete()
    return redirect('todo_list')