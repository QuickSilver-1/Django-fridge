from .models import Product, ListAccess, List, FridgeProduct, Profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
import json
import chestniy_znak
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .forms import *
from .qr_scanner import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

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

    return render(request, 'product_list/show_list.html', {"lists": lists})

def show_FridgeProduct(request):
    fridge_id = Profile.objects.get(user=request.user).fridge_id()
    products = FridgeProduct.objects.filter(user_id=fridge_id)
    return render(request, 'product_list/show_FridgeProduct.html', {"products": products})

"""
filename = 'qr_parser/test_files/photo_2023-02-06_19-03-40.jpg'
image = cv2.imread(filename)

qr = qr_parser.decode(image)
print(qr)

result = qr_parser.parse_data(qr)
print(result)
"""

def my_view_1(request):

    return render(request, 'product_list/qr_scanner.html')

def my_view(request):
    
    # View code here...
    """
    return render(request, 'product_list/receipt_scanner.html', {
        'foo': 'bar',
    }, content_type='application/xhtml+xml')
    """
    """
    filename = 'qr_parser/test_files/photo_2023-02-04_20-48-48.jpg'
    image = cv2.imread(filename)
    
    qr = qr_parser.decode(image)[0]
    """
    fn = request.GET.get("fn")
    i = request.GET.get("i")
    fp = request.GET.get("fp")

    result = parse_data_1(fn, i, fp)
    soup = BeautifulSoup(result, "html.parser")
    json_result = requests.get(soup.find("a", "msohide")["href"], headers={'Content-type': 'application/json'})
    json_result = json.loads(json_result.text)
    """
    for i in json_result['Document']['Items']:
        entry = Product(name=i['Name'], amount=i['Quantity'])
        entry.save()
    """
    #for item in result:

    json_items = json_result['Document']['Items']
    items = []
    for item in json_items:
        product = {
            "name": item["Name"],
            "price": item["Price"],
            "quantity": item["Quantity"],
            "total_price": item["Total"]
        }
        if item["ProductCode"]:
            if item["ProductCode"]['Code_GS_1M']:
                lib = chestniy_znak.Lib()
                data = lib.infoFromDataMatrix(item["ProductCode"]['Code_GS_1M'])
                product["attribute"] = data


        items.append(product)
    
    fridge_id = Profile.objects.get(user=request.user).fridge_id()

    for item in items:
        FridgeProduct.objects.create(name=item["name"], user_id=fridge_id)


    return render(request, 'product_list/receipt_scanner.html', {
        'foo': result, 
        'json': json_items,
        'items' : items
    })

def redirect_to_user(request):
    if request.user.is_authenticated:
        return redirect('qr_scanner')
    else:
        return redirect('autorisation')


class RegisterUser1(CreateView):
    extra_context = {'n': 1, 'button': 'Далее', 'back': 'autorisation'}
    form_class = RegisterForm1
    template_name = 'registration/register_user.html'

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('register2'))

    def get_success_url(self) -> str:
        return reverse_lazy('register2')

class RegisterUser2(CreateView):
    extra_context = {'n': 2, 'button': 'Зарегестрироваться', 'back': 'register'}
    form_class = RegisterForm2
    template_name = 'registration/register_user.html'
    
    def form_valid(self, form):
        post = User.objects.get(username=self.request.user)
        post.first_name = form.data['first_name']
        post.last_name = form.data['last_name']
        post.email = form.data['email']

        post.save()
        return HttpResponseRedirect(reverse_lazy('hello'))
    
def autorisation(request):
    return render(request, 'registration/autorisation.html')

def hello(request):
    return render(request, 'registration/hello.html')