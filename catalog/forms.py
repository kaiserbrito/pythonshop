from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required.'),
    last_name = forms.CharField(max_length=30, help_text='Required'),
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid e-mail address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)
