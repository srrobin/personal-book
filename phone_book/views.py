from django.shortcuts import render,redirect
from .models import PhoneBookModel,Category
from .forms import PhoneBookForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

@login_required
def home3(request):
    pb_obj = PhoneBookModel.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(pb_obj, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users':users,"phone_page": "active"}
    return render(request,'pb/phoneb.html',context)

@login_required
def add_pn(request):
    if request.method == 'POST':
        form = PhoneBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home3')
    else:
        form = PhoneBookForm()
        return render(request,'pb/add_pn.html',{'form': form})

@login_required
def detail_pn(request,pn_id):
    pn_obj = PhoneBookModel.objects.get(id=pn_id)
    context = {'pn':pn_obj}
    return render(request, 'pb/datail_pn.html',context)


@login_required
def delete_pn(request,pn_id):
    pb_obj = PhoneBookModel.objects.get(id=pn_id)
    pb_obj.delete()
    return redirect('home3')



@login_required
def edit_pn(request,pn_id):
    pb_obj = PhoneBookModel.objects.get(id=pn_id)
    form = PhoneBookForm(instance=pb_obj)
    if request.method == 'POST':
        form = PhoneBookForm(request.POST, instance=pb_obj)
        if form.is_valid():
            form.save()
            return redirect('home3')
    context = {'form': form}
    return render(request, 'pb/add_pn.html', context)

@login_required
def category_list(request):
    ctg_obj = Category.objects.all()
    context = {'ctgs':ctg_obj}
    return render(request,'pb/category-list.html',context )



#def pn_by_category(request,category_name):
     #ctg_obj = Category.objects.get(name=category_name)
     #pn_obj = PhoneBookModel.objects.filter(ctg=ctg_obj)
     #context = {'ctg_det_all':pn_obj,'ctg_name':category_name}
     #return render(request,'pb/category-detail.html',context)
