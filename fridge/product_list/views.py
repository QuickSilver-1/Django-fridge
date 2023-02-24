from django.shortcuts import render
from .models import Product, ListAccess, List, FridgeProduct
from user.models import Profile
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def show_list(request):
    access = ListAccess.objects.filter(user=request.user)
    lists = []
    for lst_access in access:
        lst = List.objects.get(id=lst_access.id)
        products = Product.objects.filter(list_id=lst.id)
        for p in products:
            print(products)
        print()
        #lists.append()
    print(Profile.objects.get(user=request.user).fridge_id())

    return render(request, 'show_list.html', {"lists": lists})

def show_FridgeProduct(request):
    fridge_id = Profile.objects.get(user=request.user).fridge_id()
    products = FridgeProduct.objects.filter(user_id=fridge_id)
    for i in products:
        print(products)
    return render(request, 'show_FridgeProduct.html', {"products": products})