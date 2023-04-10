from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "TodoApp/home.html", {})

def addList(request):
    return render(request, "TodoApp/addList.html", {})

