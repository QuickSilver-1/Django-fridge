from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Ivanov_123'})),
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form'})),
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form'})),
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Иван'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Иванов'})),
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'forexample@gmail.com'})),

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Введите имя пользователя',
            'password1': 'Придумайте свой пароль',
            'password2': 'Подтвердите пароль',
            'first_name': 'Введите ваше имя',
            'last_name': 'Введите вашу фамилию',
            'email': 'Введите адрес электронной почты',
        }
        
        