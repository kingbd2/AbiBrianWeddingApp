from api.models import Guest, Party
from django.core.management.base import BaseCommand
from api.email_invitations import send_invitation


c = {'name': Party.name}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        c = {'name': Party.name}
        send_invitation(c)
        print("Email sent")
