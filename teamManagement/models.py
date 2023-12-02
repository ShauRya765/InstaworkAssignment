# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class TeamMemberManager(BaseUserManager):
    def create_team_member(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        team_member = self.model(email=email, **extra_fields)
        team_member.set_password(password)
        team_member.save(using=self._db)
        return team_member

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_team_member(email, password, **extra_fields)


class TeamMember(AbstractUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('regular', "Regular"),
        ('admin', "Admin"),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='regular')

    objects = TeamMemberManager()

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        # Set the username to be the same as the email
        self.username = self.email
        super().save(*args, **kwargs)
