from django.db import models


# Create your models here.

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('regular', "Regular"),
        ('admin', "Admin ")
    ]

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='regular')
