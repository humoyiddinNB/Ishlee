from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import authenticate


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password' : forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and confirm_password != password:
            raise ValidationError("Parollar mos emas!")

        return cleaned_data


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not User.objects.filter(username=username).exists():
            raise ValidationError("Bunday username egasi yo‘q!")

        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError("Parol noto‘g‘ri!")

        return cleaned_data
