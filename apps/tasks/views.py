from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import TaskForm
from .models import Task

@login_required(login_url='accounts/login')
def task_list(request):
    search = request.GET.get('search')

    if search:
        tasks = Task.objects.filter(title__icontains=search, user=request.user)
    else:
        task_list = Task.objects.all().order_by('-created_at').filter(user=request.user)

        paginator = Paginator(task_list, 3)
        page = request.GET.get('page')

        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required(login_url='accounts/login')
def task_view(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required(login_url='accounts/login')
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.user = request.user
            task.save()

            return redirect('/')

    form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

@login_required(login_url='accounts/login')
def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

@login_required(login_url='accounts/login')
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')