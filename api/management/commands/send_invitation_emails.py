from api.models import Guest, Party
from django.core.management.base import BaseCommand
from api.email_invitations import send_invitation


c = {'name': Party.name}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = Party.objects.all()
        # filter(name="King").values()
        i = 0
        for item in data:
            guests = list(Guest.objects.filter(party=item).values('first_name'))
            print(guests[0]["first_name"])
            i = i+1
            if i == 1:
                break
        # i = 0
        # for item in data:
        #     c = {'name': item}
        #     send_invitation(c)
        #     i = i+1
        #     print(item)
        #     if i == 1:
        #         break
        # send_invitation(c)
        # print("Email sent")
