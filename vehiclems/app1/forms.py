from django.contrib.auth.forms import UserCreationForm


from app1.models import User1
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User1
        fields = UserCreationForm.Meta.fields