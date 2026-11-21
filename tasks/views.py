from django.shortcuts import render,get_object_or_404, redirect
from .models import Tasks
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Tasks.objects.all().order_by('-created')
    return render(request,"tasks/task_list.html",{"tasks": tasks})

def task_detail(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    return render(request,"tasks/task_detail.html",{"task": task})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list");
    else:
        form = TaskForm()

    return render(request,"tasks/task_form.html",{"form":form})

def edit_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail",pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(request,"tasks/task_form.html",{"form" : form})

def delete_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request,"tasks/task_confirm_delete.html",{"task":task})