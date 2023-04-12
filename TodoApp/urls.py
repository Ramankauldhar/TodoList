from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/",home),
    path("addList/",addList),
    path("deleteList/<int:id>",deleteList),
    path("updateList/<int:id>",updateList),
]