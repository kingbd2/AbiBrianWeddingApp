from api.models import Guest, Party
from django.core.management.base import BaseCommand
from api.email_invitations import send_invitation


c = {'name': Party.name}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # data = Party.objects.all()
        data = list(Party.objects.values('name', 'email', 'invitation_id'))
        i = 0
        test_emails = ['kingbd2@gmail.com']
        # test_emails = ['alison_king_85@hotmail.com', 'kingbd2@gmail.com']
        # data = list(Party.objects.filter(blog_id=4))

        for item in test_emails:
            test_data = list(Party.objects.filter(
                email=item).values('name', 'email', 'invitation_id'))
            print(test_data)

            email = test_data[0]['email']
            print(email)
            invitation_id = test_data[0]['invitation_id']
            # print(invitation_id)
            first_name = list(Guest.objects.filter(
                party=test_data[0]['name']).values('first_name'))
            last_name = list(Guest.objects.filter(
                party=test_data[0]['name']).values('last_name'))

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
                    print(first_name_text)

            c = {
                'first_name_text': first_name_text,
                'last_name': last_name,
                'invitation_id': invitation_id}
            send_invitation(c, email)
            print("Email sent")
            i = i+1
            if i == 2:
                break
