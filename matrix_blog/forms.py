from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
User = get_user_model()

# from django.contrib.auth.models import User
from .models import Comment

class RegisterForm(UserCreationForm):
    first_name = forms.CharField( max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class AddNewForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    body = forms.CharField(label="Body", widget=forms.Textarea)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']