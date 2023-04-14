from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'content',
            'movie',
        )


class CommentForm(forms.ModelForm):
    # content = forms.Textarea(
    #     widget=forms.TextInput(attrs={
    #         'rows': 7,
    #         'cols': 7,
    #     })
    # )
    class Meta:
        model = Comment
        fields = (
            'content',
        )
