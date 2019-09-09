from django.db import models
from datetime import date
from django.db.models.fields import TimeField

class Type(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Todo(models.Model):
     task_title = models.CharField(max_length=300)
     ctg = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
     reminder = models.TimeField(null=True)
     date = models.DateField(null=True)
     task_des = models.TextField()
     completed = models.BooleanField(default=False)


     def __str__(self):
         return self.task_title




