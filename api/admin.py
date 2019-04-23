from django.contrib import admin

from .models import CustomUser, Guest, Role
admin.site.register([CustomUser, Guest, Role])
