from django import forms
from django.contrib.auth.models import User
from cosmos.models import Post

class GenericUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UpdateUserForm(GenericUserForm):
    username = forms.CharField(max_length=150, label='New Username')
    password = forms.CharField(label='New Password', widget=forms.PasswordInput)

class CreateUserForm(GenericUserForm):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CreatePostForm(forms.ModelForm):
    post_body = forms.CharField(max_length=250, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('post_body',)