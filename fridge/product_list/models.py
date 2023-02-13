from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(blank=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    amount = models.SmallIntegerField()
    date_purchase = models.DateField(auto_now_add=True)
    type = models.ForeignKey('Type', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    Spoil = models.DateTimeField()

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)
    Expiration_date = models.SmallIntegerField()

    def __str__(self):
        return self.name