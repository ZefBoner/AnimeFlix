from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UsernameField
from .models import Usuario

class CambiarInformacionForm(UserChangeForm):
    username = UsernameField(disabled=True)

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email']
