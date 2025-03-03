from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email cím",
        widget=forms.EmailInput(
            attrs={
                "class": "bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    username  = forms.CharField(
        required=True,
        label="Felhasználónév",
        widget=forms.TextInput(
            attrs={
                "class": "bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    password1  = forms.CharField(
        required=True,
        label="Jelszó",
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )
    password2  = forms.CharField(
        required=True,
        label="Jelszó újra",
        widget=forms.PasswordInput(
            attrs={
                "class": "bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Felhasználónév'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 mb-3 mt-1.5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': 'Jelszó'})
    )
