from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'select2_content',)
        label_suffix = ''
    
    title = forms.CharField(label='주제', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    select1_content = forms.CharField(label='왼쪽', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    select2_content = forms.CharField(label='오른쪽', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))