from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from tasks.forms import TaskForm

@login_required
def tasks_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks_list')
    return render(request, 'tasks/confirm_delete.html')