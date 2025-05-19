from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=30, required=False)
    last_name  = forms.CharField(label='Last Name',  max_length=30, required=False)
    email      = forms.EmailField(label='Email', required=True)

    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    # you can override widgets or labels here if you like
    old_password   = forms.CharField(label='Current Password',
                                     widget=forms.PasswordInput)
    new_password1  = forms.CharField(label='New Password',
                                     widget=forms.PasswordInput)
    new_password2  = forms.CharField(label='Confirm New Password',
                                     widget=forms.PasswordInput)