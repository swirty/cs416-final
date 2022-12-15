from django import forms
from cosmos.models import Post


class create_post_form(forms.ModelForm):
    post_body = forms.CharField(max_length=250, widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('post_body',)
