from django.contrib import admin

from .models import CustomUser, Guest, Role, Party, Event, Location
admin.site.register([Guest, Party, Role, Event, Location])
