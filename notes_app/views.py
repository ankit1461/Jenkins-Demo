from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'notes/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'notes/add_task.html')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')

    return render(request, 'notes/update_task.html', {'task': task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def start_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_active = True
    task.start_time = timezone.now()
    task.end_time = None
    task.save()
    return redirect('task_list')

def end_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_active = False
    task.end_time = timezone.now()
    task.save()
    return redirect('task_list')
