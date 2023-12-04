# teams/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import RadioSelect

from .models import TeamMember


# Form for adding/editing Team Members
class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'role']

        # Explicitly set the widget for the 'role' field to RadioSelect
        widgets = {
            'role': RadioSelect()
        }


# Form for user registration, extends Django's UserCreationForm
class RegistrationForm(UserCreationForm):
    # Additional fields for first name and last name
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = TeamMember
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']

    # Custom validation for the email field to check for uniqueness
    def clean_email(self):
        email = self.cleaned_data['email']
        existing_user = TeamMember.objects.filter(email=email).exclude(pk=self.instance.pk).first()
        if existing_user:
            raise ValidationError("This email is already in use.")
        return email

    # Custom save method to set the default role to 'regular'
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'regular'
        if commit:
            user.save()
        return user


# Form for user login, extends Django's AuthenticationForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = TeamMember
        fields = ['username', 'password']
