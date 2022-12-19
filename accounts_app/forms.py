import django_resized.forms
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

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



class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'pro_pic', 'banner_pic']
    about = forms.CharField(max_length=250, label='About Me', required=False)
    pro_pic = forms.ImageField(label='Profile Picture', required=False)
    banner_pic = forms.ImageField(label='Banner Picture', required=False)



class EditProfileAboutForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about']
    about = forms.CharField(max_length=250, label='About Me', widget=forms.Textarea(attrs={'class': 'cosmos-text-input'}))



class EditProfileProPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pro_pic']
    pro_pic = forms.ImageField(label='Profile Picture', required=True)



class EditProfileBannerPicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['banner_pic']
    banner_pic = forms.ImageField(label='Banner Picture', required=True)