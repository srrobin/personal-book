from django.shortcuts import render,redirect
from django.contrib.auth.models import User


def home(request):
    userobj = User.objects.count()
    return render(request,'home.html',{'count':userobj})

