from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    todo_list = Todo.objects.order_by('id')
    page = request.GET.get('page', 1)

    paginator = Paginator(todo_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users':users ,"todo_page": "active"}
    return render(request,'todo/home.html',context)

@login_required
def add_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoHome')
    context = {'form':form}
    return render(request, 'todo/add-todo.html', context)


@login_required
def edit_todo(request,todo_id):
    todo_obj = Todo.objects.get(id=todo_id)
    form = TodoForm(instance=todo_obj)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo_obj)
        if form.is_valid():
            form.save()
            return redirect('todoHome')
    context = {'form': form}
    return render(request, 'todo/add-todo.html', context)


@login_required
def details_todo(request,todo_id):
    todo_obj = Todo.objects.get(id=todo_id)
    context = {'todo':todo_obj}
    return render(request,'todo/detail.html',context)


@login_required
def cross_off(request,todo_id):
    item = Todo.objects.get(id=todo_id)
    item.completed = True
    item.save()

    return redirect('todoHome')

@login_required
def uncross(request,todo_id):
    item = Todo.objects.get(id=todo_id)
    item.completed = False
    item.save()

    return redirect('todoHome')

@login_required
def deleteCompleted(request):
    Todo.objects.filter(completed__exact=True).delete()

    return redirect('todoHome')


@login_required
def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('todoHome')