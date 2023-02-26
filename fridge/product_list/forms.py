from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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

        self.fields['email'].label = mark_safe('<h3>Введите свой email</h3>')

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'register-form', 'placehodler':'forexample@gmail.com'})),

    class Meta:
        model = User
        fields = ('email',)
        labels = {
            'email': 'Введите адрес электронной почты',
        }

class LoginForm(AuthenticationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = mark_safe('<h3>Имя пользователя</h3>')
        self.fields['password'].label = mark_safe('<h3>Пароль</h3>')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'login-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login-field'}))
