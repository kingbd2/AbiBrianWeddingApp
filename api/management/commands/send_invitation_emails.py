from api.models import Guest, Party
from django.core.management.base import BaseCommand
from api.email_invitations import send_invitation


c = {'name': Party.name}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # data = Party.objects.all()
        data = list(Party.objects.values('name', 'email', 'invitation_id'))
        i = 0
        for item in data:
            invitation_id = item['invitation_id']
            # print(invitation_id)
            first_name = list(Guest.objects.filter(
                party=item['name']).values('first_name'))
            last_name = list(Guest.objects.filter(
                party=item['name']).values('last_name'))

            if len(first_name) == 1:
                first_name_text = first_name[0]['first_name']
                print(first_name_text)
            elif len(first_name) == 2:
                first_name_text = first_name[0]['first_name'] + \
                    " and " + \
                    first_name[1]['first_name']
                print(first_name_text)
            else:
                j = 0
                first_name_text = ''
                for name in first_name:
                    if j == (len(first_name)-1):
                        first_name_text = first_name_text + \
                            'and ' + first_name[j]['first_name']
                    else:
                        first_name_text = first_name_text + \
                            first_name[j]['first_name'] + ', '
                    j = j + 1
                    # print(first_name_text)

            c = {
                'first_name_text': first_name_text,
                'last_name': last_name,
                'invitation_id': invitation_id}
            send_invitation(c)
            print("Email sent")
            i = i+1
            if i == 10:
                break
