from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import Comment


class RegisterForm(UserCreationForm):
    first_name = forms.CharField( max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']