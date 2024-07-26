from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import *

# Create your views here.


def receipes(request):
    if request.method=='POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        Receipe.objects.create(receipe_name=receipe_name,receipe_description=receipe_description,receipe_image=receipe_image)
        return redirect('/receipes/')
    


    query_set=Receipe.objects.all()

    if request.method=='GET':
        if request.GET.get('search_re'):
            print('hello')
            print(request.GET.get('search_re'))
            query_set=query_set.filter(receipe_name__icontains=request.GET.get('search_re'))
            print(query_set)
    context={'receipes':query_set}

        
    return render(request,'receipes.html',context)
        



def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)

    if request.method=='POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image
        
        queryset.save()

        return redirect('/receipes/')
        
    context={'receipe':queryset}
    
    return render(request,'update_receipe.html',context)



def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()





def login_page(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        
        user=authenticate(username=username,password=password)

        if user is not None:
            print('invalid credentails ')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/reciepes/')

        
        



    return render(request,'login.html')

def register_page(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            print('username already taken')
            messages.info(request,'username is already taken')
            return redirect("/register")
    
        user=User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()
        messages.info(request,'account create successfully')
        return redirect('/register/')
    return render(request,'register.html')
    
    
    
