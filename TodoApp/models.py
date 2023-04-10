from django.db import models

# Create your models here.

class TodoList(models.Model):
    task = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    date = models.CharField(max_length=20)

