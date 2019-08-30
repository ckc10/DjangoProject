from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["firstname"]
        user.last_name = self.cleaned_data["lastname"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    current_employer = forms.CharField()
    total_experience = forms.CharField()

    class Meta:
        model = Profile
        fields = ['current_employer', 'total_experience']
