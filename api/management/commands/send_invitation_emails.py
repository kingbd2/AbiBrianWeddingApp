from api.models import Guest, Party
from django.core.management.base import BaseCommand
from api.email_invitations import send_invitation

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        send_invitation()
        print("Email sent")
