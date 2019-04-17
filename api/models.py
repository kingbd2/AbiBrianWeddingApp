from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import uuid
from postgres_copy import CopyManager


class Party(models.Model):
        """
        A party consists of one or more guests.
        """
        name = models.TextField()
        save_the_date_sent = models.DateTimeField(null=True, default=None)
        is_invited = models.BooleanField(default=False)
        is_attending = models.NullBooleanField(default=None)


class Role(models.Model):
    role_name = models.TextField(null=True, blank=True)


class CustomUser(AbstractUser):
        """
        A single guest
        """
        party = models.ForeignKey(Party, on_delete=models.CASCADE, null=True)
        first_name = models.TextField(null=True, blank=True)
        last_name = models.TextField(null=True, blank=True)
        email = models.EmailField(
            verbose_name='email address',
            max_length=255,
            unique=True,
        )
        is_attending = models.NullBooleanField(default=None)
        invited = models.BooleanField(default=False, null=True)
        # invitation_id = models.UUIDField(
        #     primary_key=True, default=uuid.uuid4, editable=False)
        invitation_sent = models.DateTimeField(
            null=True, blank=True, default=None)
        invitation_opened = models.DateTimeField(
            null=True, blank=True, default=None)
        title = models.CharField(blank=True, null=True, max_length=3)
        date_joined = models.DateField(auto_now_add=True, null=True)

        password = models.TextField(null=True, blank=True)
        last_login = models.DateTimeField(
            null=True, blank=True, default=None)
        is_superuser = models.BooleanField(default=False)
        username = models.TextField(null=True, blank=True, unique=True)
        created = models.DateField(auto_now_add=True, null=True)

        role = models.ForeignKey(
            Role, on_delete=models.CASCADE, null=True)

        # objects = CopyManager()

        def __str__(self):
                return self.first_name


class Location(models.Model):
        location_name = models.CharField(blank=True, max_length=100)
        city = models.CharField(blank=True, max_length=100)
        street_num = models.CharField(blank=True, max_length=100)
        sreet_name = models.CharField(blank=True, max_length=100)
        postal_code = models.CharField(blank=True, max_length=6)


class Event(models.Model):
        event_name = models.CharField(blank=True, max_length=100)
        date = models.DateField()
        start_time = models.DateField(auto_now=True)
        end_time = models.DateField(auto_now=True)
        details = models.TextField()
        location_id = models.ForeignKey(
            Location, on_delete=models.CASCADE, null=True)
