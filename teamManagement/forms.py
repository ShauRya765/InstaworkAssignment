# teams/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import RadioSelect

from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']

        # Explicitly set the widget for the 'role' field
        widgets = {
            'role': RadioSelect()
        }


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        existing_user = TeamMember.objects.filter(email=email).exclude(pk=self.instance.pk).first()
        if existing_user:
            raise ValidationError("This email is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'regular'
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = TeamMember
        fields = ['username', 'password']
