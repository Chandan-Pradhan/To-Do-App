from django.shortcuts import render
from django.utils import timezone
from .models import ToDo
from django.http import HttpResponseRedirect


def display(request):
    todo_items = ToDo.objects.all().order_by("-added_date")
    return render(request, 'index.html', {"todo_items": todo_items})


def add_todo(request):
    current_addeddate = timezone.now()
    content = request.POST["content"].capitalize()
    print(request.POST)
    created_obj = ToDo.objects.create(added_date=current_addeddate, text=content)
    return HttpResponseRedirect("/")


def delete(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")



