from django.shortcuts import render,redirect
from .models import DiaryModel
from .forms import DiaryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required
def home2(request):
    diary_obj = DiaryModel.objects.order_by('-date')
    page = request.GET.get('page', 1)

    paginator = Paginator(diary_obj, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {'users': users,"dairy_page": "active"}
    return render(request, 'diary/diary.html', context)

@login_required
def detail(request, diary_id):
    diary_obj = DiaryModel.objects.get(id=diary_id)
    context = {'diary': diary_obj}
    return render(request, 'diary/detail.html', context)

@login_required
def add_diary(request):
    form = DiaryForm()
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home2')
    context = {'form': form}
    return render(request, 'diary/add.html', context)

@login_required
def edit_diary(request, diary_id):
    diary_obj = DiaryModel.objects.get(id=diary_id)
    form = DiaryForm(instance=diary_obj)
    if request.method == 'POST':
        form = DiaryForm(request.POST, instance=diary_obj)
        if form.is_valid():
            form.save()
            return redirect('home2')
    context = {'form': form}
    return render(request, 'diary/add.html', context)

@login_required
def delete_diary(request, diary_id):
    diary_obj = DiaryModel.objects.get(id=diary_id)
    diary_obj.delete()
    return redirect('home2')
