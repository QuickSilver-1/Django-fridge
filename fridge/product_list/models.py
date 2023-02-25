from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

class ListAccess(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, null=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)   
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, null=False, blank=True)

    def __str__(self):
        return self.name

class FridgeProduct(models.Model):
    name = models.CharField(max_length=500)   
    user_id = models.IntegerField(null=True, blank=True)
