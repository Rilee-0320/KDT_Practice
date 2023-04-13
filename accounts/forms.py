from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class CustomUserChangeForm(UserChangeForm):
    # email = forms.EmailField(required=True)
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
        )