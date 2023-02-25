from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe

class RegisterForm1(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = mark_safe('<h3>Введите имя пользователя</h3>')
        self.fields['password1'].label = mark_safe('<h3>Введите пароль</h3>')
        self.fields['password2'].label = mark_safe('<h3>Подтвердите пароль</h3>')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Ivanov_123'})),
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form'})),
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form'})),

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        
class RegisterForm2(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].label = mark_safe('<h3>Введите своё имя</h3>')
        self.fields['last_name'].label = mark_safe('<h3>Введите свою фамилию</h3>')
        self.fields['email'].label = mark_safe('<h3>Введите свой email</h3>')

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Иван'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'Иванов'})),
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'forexample@gmail.com'})),

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Введите ваше имя',
            'last_name': 'Введите вашу фамилию',
            'email': 'Введите адрес электронной почты',
        }