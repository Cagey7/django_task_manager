from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description")


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        # widgets = {
        #     "email": forms.TextInput(attrs={"style": "width: 1000px"}),
        #     "password1": forms.TextInput(attrs={"style": "width: 1000px"})
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    