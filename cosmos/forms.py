from django import forms
from cosmos.models import Post

class CreatePostForm(forms.ModelForm):
    post_body = forms.CharField(max_length=250, widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('post_body',)