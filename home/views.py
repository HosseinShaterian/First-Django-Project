from django.shortcuts import render, redirect
from .models import CustomerRequest
from django.contrib import messages
from .forms import CustomerRequestCreateForm, CustomerRequestUpdateForm

# Create your views here.


def home(request):
    all=CustomerRequest.objects.all()
    return render(request,'home.html',{'allRequest':all})


def hello(request):
    person={'name':'mamad'}
    return render(request,'hello.html',context=person)

def detail(request, request_id):
    req=CustomerRequest.objects.get(id=request_id)
    # return render(request, 'detail.html', 'req':req)
    return render(request,'detail.html',{'req':req})

def delete(request, request_id):
    CustomerRequest.objects.get(id=request_id).delete()
    messages.success(request, 'درخواست با موفقیت حذف شد...', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form=CustomerRequestCreateForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            CustomerRequest.objects.create(name=cd['name'], address=cd['address'], phone=cd['phone'], type_of_service=cd['type_of_service'], device_name=cd['device_name'], request_date=cd['request_date'], is_done=cd['is_done'])
            messages.success(request, 'created successful', 'success')
            return redirect('home')
    else:
        form= CustomerRequestCreateForm()
    return render(request, 'create.html', {'form':form})

def update(request, request_id):
    req=CustomerRequest.objects.get(id=request_id)
    if request.method == 'POST':
        form=CustomerRequestUpdateForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            messages.success(request, 'update successfull', 'success')
            return redirect('details', request_id)
    else:
        form=CustomerRequestUpdateForm(instance=req)
    return render(request, 'update.html', {'form':form})