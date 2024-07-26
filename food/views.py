from django.shortcuts import render,redirect

# Create your views here.

from food.models import *

def dishes(request):

    if request.method=='POST':
        data=request.POST
        dish_name=data.get('dish_name')
        dish_description=data.get('dish_description')
        dish_image=request.FILES.get('dish_image')
        print('***')
        print(dish_image)
        
        Dish.objects.create(dish_name=dish_name,dish_description=dish_description,dish_image=dish_image)
        return redirect('/dishes/')
    

    query_set=Dish.objects.all()
    context={"dishes":query_set}

    return render(request,'dishes.html',context)


def delete_dish(request,id):
    queryset=Dish.objects.get(id=id)
    queryset.delete()
    return redirect('/dishes/')
    

def update_dish(request,id):
    queryset=Dish.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        dish_name=data.get('dish_name')
        dish_description=data.get('dish_description')
        dish_image=request.FILES.get('dish_image')

        print(dish_name)
        print(dish_description)

        queryset.dish_name=dish_name
        queryset.dish_description=dish_description

        if dish_image:
            queryset.dish_image=dish_image
        

        queryset.save()

        return redirect('/dishes/')

    context={'dishes':queryset}
    
    return render(request,'update_dish.html',context)
