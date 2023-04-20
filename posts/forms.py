from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content', 'image1', 'select2_content', 'image2')
        label_suffix = ''
    
    title = forms.CharField(label='주제', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    select1_content = forms.CharField(label='왼쪽', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    select2_content = forms.CharField(label='오른쪽', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 200px;'}))
    

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs={
                'placeholder' : '댓글 작성',
                'class': 'form-control',
                'style': 'width: 80%; display: inline-flex;',
            },
        ),
    )
    class Meta:
        model = Comment
        fields = ('content',)
        label_suffix=''