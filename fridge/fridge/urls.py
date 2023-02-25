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
from receipt_scanner.views import *
from product_list.views import show_list, show_FridgeProduct
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', redirect_to_user),
    path('admin/', admin.site.urls),
    path('user/login/', LoginView.as_view(), name='login'),
    path('user/', include('django.contrib.auth.urls')),
    path('receipt_scanner/', my_view),
    path('qr_scanner/', my_view_1, name='qr_scanner'),
    path('product_list/', show_list),
    path('fridge/', show_FridgeProduct),
    path('user/register/', RegisterUser.as_view(), name='register'),
]
