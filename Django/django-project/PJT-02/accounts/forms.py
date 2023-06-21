from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name','birthday', 'password1', 'password2')

    birthday = forms.DateField(
        label='생년월일',
        widget = forms.DateInput(
            attrs={'type': 'date'},
        ),
    )
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name','birthday')

    birthday = forms.DateField(
        label='생년월일',
        widget = forms.DateInput(
            attrs={'type': 'date'},
        ),
    )