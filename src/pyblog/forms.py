from django import forms
from pyblog.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')