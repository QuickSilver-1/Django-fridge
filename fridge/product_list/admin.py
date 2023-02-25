from django.contrib import admin
from .models import Product, Profile, ListAccess, List, FridgeProduct


admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(FridgeProduct)
admin.site.register(ListAccess)
admin.site.register(List)
# Register your models here.
