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
        name = models.TextField(primary_key=True)
        save_the_date_sent = models.DateTimeField(null=True, default=None)
        is_invited = models.BooleanField(null=True, blank=True, default=False)
        is_attending = models.NullBooleanField(null=True, blank=True, default=None)
        category = models.CharField(max_length=20, null=True, blank=True)
        invitation_id = models.UUIDField(
            default=uuid.uuid4, editable=False)
        invitation_sent = models.DateTimeField(
            null=True, blank=True, default=None)
        invitation_opened = models.DateTimeField(
            null=True, blank=True, default=None)
        rehearsal_dinner = models.BooleanField(null=True, blank=True, default=False)
        comments = models.TextField(null=True, blank=True)
        objects = CopyManager()

        def __str__(self):
                return self.name


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
        is_superuser = models.BooleanField(default=False)
        is_primarycontact = models.BooleanField(default=False)
        iskid = models.BooleanField(default=False)
        hasguest = models.BooleanField(default=False)
        group = models.CharField(blank=True, null=True, max_length=50)
        first_name = models.CharField(blank=True, null=True, max_length=50)
        last_name = models.CharField(blank=True, null=True, max_length=50)
        email = models.EmailField(
            verbose_name='email address',
            max_length=255,
        )
        is_attending = models.NullBooleanField(default=None)
        role = models.ForeignKey(
                Role, on_delete=models.CASCADE, null=True)
        objects = CopyManager()

        def __str__(self):
                return '{} {}'.format(self.first_name, self.last_name)


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
