from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, label=_("Username"))
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'), validators=[validate_password])

    remember_me = forms.BooleanField(required=False, initial=False, label=_("Remember me"))

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data['username']
        password = cleaned_data['password']

        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError(_("User not found."))

        self.cleaned_data['user'] = user
