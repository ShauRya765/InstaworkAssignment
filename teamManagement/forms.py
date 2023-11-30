# teams/forms.py
from django import forms
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
