from django.shortcuts import render,redirect
from .models import TodoList

# Create your views here.

def home(request):
    list = TodoList.objects.all()
    return render(request, "TodoApp/home.html", {'list':list})

def addList(request):
    if request.method == 'POST':
        print("New Task Entry Added in The Database")

        #retrieve the user inputs 
        user_task = request.POST.get("task")
        user_description = request.POST.get("description")
        user_date = request.POST.get("dateandtime")

        #create an object for models
        list = TodoList()
        list.task = user_task
        list.description = user_description
        list.date = user_date
        list.save()
        return redirect("/TodoApp/home")

    return render(request, "TodoApp/addList.html", {})

def deleteList(request, id):
    list = TodoList.objects.get(pk=id)
    list.delete()
    return redirect("/TodoApp/home")

def updateList(request, id):
    list = TodoList.objects.get(pk=id)
    return render(request, "TodoApp/updateList.html", {'list':list})

def update(request, id):
    user_task = request.POST.get("task")
    user_description = request.POST.get("description")
    user_date = request.POST.get("dateandtime")
    
    list = TodoList.objects.get(pk=id)
    list.task = user_task
    list.description = user_description
    list.date = user_date
    list.save()
    return redirect("/TodoApp/home")


