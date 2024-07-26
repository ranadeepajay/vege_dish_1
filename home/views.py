from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):

    peoples=[

        {'name':'abhi','age':26},
        {'name':'abi','age':25},
        {'name':'vniy','age':24},
        {'name':'sandeep','age':14}

    ]

    vegitables=[
        'tomato',
        'potato', 'alu'
    ]
    return  render(request,'index.html',context={'peoples':peoples})



def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')