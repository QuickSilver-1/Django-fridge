from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fridge_refer = models.IntegerField(null=True, blank=True)

    def fridge_id(self):
        if self.fridge_refer == None:
            return self.user.id
        else:
            return self.fridge_refer

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()