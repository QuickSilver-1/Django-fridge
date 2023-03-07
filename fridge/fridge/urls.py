"""fridge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
from product_list.views import *


urlpatterns = [
    path('', redirect_to_user),
    path('admin/', admin.site.urls),
    path('user/login/', LoginUser.as_view(), name='login'),
    path('user/', include('django.contrib.auth.urls')),
    path('receipt_scanner/', my_view),
    path('qr_scanner/', my_view_1, name='qr_scanner'),
    path('qr_scanner/', my_view_1, name='qr_scanner'),
    path('product_list/', show_list),
    path('fridge/', show_FridgeProduct, name='fridge'),
    path('user/register/', RegisterUser1.as_view(), name='register'),
    path('user/register2/', RegisterUser2.as_view(), name='register2'),
    path('user/authorisation/', authorisation, name='authorisation'),
    path('user/hello/', hello, name='hello'),
    path('my_product/', my_product, name='my_product'),
    path('methods/delete_FridgeProduct/<p_id>', Methods.delete_FridgeProduct),
    path('my_lists/', my_lists),
    
]
