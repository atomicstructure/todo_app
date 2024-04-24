from django.shortcuts import render, redirect
from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {'tasks': tasks, 'completed_tasks': completed_tasks}
    return render(request, 'home.html', context)

def add_task(request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('home')

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')