from django import forms
from .models import Post
from datetime import datetime

class PostForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력칸',
                'class': 'form-control'
            }
        ),
        required=True
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'placeholder': '내용 입력',
                'class': 'my-content form-control'
            }
        ),
        required=True
    )
    category = forms.ChoiceField(
        label='카테고리',
        widget=forms.Select(
            attrs={
                'placeholder': '카테고리 입력',
                'class': 'form-select',
            }
        ),
        choices = (('개발','개발'), ('신기술', '신기술'), ('CS','CS')),
        required=True,
    )

    dt_now = datetime.today().strftime('%Y-%m-%d')
    deadline = forms.DateField(
        label='마감기한',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': 'date',
                'value': dt_now,
            }
        ),
        required=True
    )

    class Meta:
        model = Post
        fields = '__all__'
