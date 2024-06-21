from django.shortcuts import render, redirect


from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = TaskForm()
    tasks = Task.objects.filter(is_done=False)
    context = {"tasks": tasks, "form": form}

    return render(request, "task/index.html", context=context)


# deleting task view


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect("/")


def mark_as_done(request, task_id):
    tasks = Task.objects.get(pk=task_id)
    tasks.is_done = True
    tasks.save()
    message = "Task marked as done"
    return redirect("/")
