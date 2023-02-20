from django.shortcuts import render
from .models import Product
#from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def show_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'show_list.html', {"products": products})