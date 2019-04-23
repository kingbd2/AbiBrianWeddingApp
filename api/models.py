from django.contrib.auth.models import (BaseUserManager, AbstractUser)
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
import uuid
from postgres_copy import CopyManager


# def _random_uuid():
#     return uuid.uuid4().hex


class Party(models.Model):
        """
        A party consists of one or more guests.
        """
        name = models.TextField()
        save_the_date_sent = models.DateTimeField(null=True, default=None)
        is_invited = models.BooleanField(default=False)
        is_attending = models.NullBooleanField(default=None)
        category = models.CharField(max_length=20, null=True, blank=True)
        invitation_id = models.UUIDField(
            primary_key=True, default=uuid.uuid4, editable=False)
        invitation_sent = models.DateTimeField(
            null=True, blank=True, default=None)
        invitation_opened = models.DateTimeField(
            null=True, blank=True, default=None)
        is_invited = models.BooleanField(default=False)
        rehearsal_dinner = models.BooleanField(default=False)
        comments = models.TextField(null=True, blank=True)


class Role(models.Model):
    role_name = models.TextField(null=True, blank=True)

    def __str__(self):
                return self.role_name


class CustomUser(AbstractUser):
        first_name = models.TextField(null=True, blank=True)
        last_name = models.TextField(null=True, blank=True)

        def __str__(self):
                return self.first_name


class Guest(models.Model):
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
        role = models.ForeignKey(
                Role, on_delete=models.CASCADE, null=True)
        objects = CopyManager()

        def __str__(self):
                return self.first_name


class Location(models.Model):
        location_name = models.CharField(blank=True, max_length=100)
        city = models.CharField(blank=True, max_length=100)
        street_num = models.CharField(blank=True, max_length=100)
        sreet_name = models.CharField(blank=True, max_length=100)
        postal_code = models.CharField(blank=True, max_length=6)


class Event(models.Model):
        role = models.ForeignKey(
            Role, on_delete=models.CASCADE, null=True)
        event_name = models.CharField(blank=True, max_length=100)
        date = models.DateField()
        start_time = models.DateField(auto_now=True)
        end_time = models.DateField(auto_now=True)
        details = models.TextField()
        location_id = models.ForeignKey(
            Location, on_delete=models.CASCADE, null=True)
