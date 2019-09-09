from django.shortcuts import render,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import AlbumForm
from .models import AlbumModel
from django.contrib.auth.decorators import login_required
@login_required
def home4(request):
    img_obj = AlbumModel.objects.order_by('id')

    page = request.GET.get('page', 1)

    paginator = Paginator(img_obj, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users, "img_page": "active"}
    return render(request,'album/album.html',context)


@login_required
def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home4')
    else:
        form = AlbumForm()
        return render(request,'album/add-image.html',{'form':form})


@login_required
def album_detail(request,pk):
    album_obj = AlbumModel.objects.get(pk=pk)
    context = {'album':album_obj}
    return render(request, 'album/detail.html', context)


@login_required
def edit_album(request,pk):
    al_obj = AlbumModel.objects.get(pk=pk)
    form =AlbumForm(instance=al_obj)
    if request.method == 'POST':
        form = AlbumForm(request.POST,instance=al_obj)
        if form.is_valid():
            form.save()
            return redirect('home4')
    context = {'form': form}
    return render(request, 'album/edit_album.html', context)


@login_required
def delete_diary(request, pk):
    album_obj = AlbumModel.objects.get(pk=pk)
    album_obj.delete()
    return redirect('home4')