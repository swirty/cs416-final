from django import forms
from django.contrib.auth.models import User

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='New Username')
    password = forms.CharField(label='New Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')