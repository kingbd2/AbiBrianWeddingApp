from django.contrib import admin

from .models import CustomUser, Guest, Role, Party
admin.site.register([Guest, Party, Role])
