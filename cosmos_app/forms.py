from django import forms
from cosmos_app.models import Post


class CreatePostForm(forms.ModelForm):
    post_body = forms.CharField(max_length=250, widget=forms.Textarea(attrs={'class': 'cosmos-text-input'}), label='Post Body')

    class Meta:
        model = Post
        fields = ['post_body',]
