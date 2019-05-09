from api.models import Guest, Party
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)

        # Insert Guest data
        insert_count_guest = Guest.objects.from_csv(
            'data/test_guest_data.csv',
            )
        print("{} test guest records inserted".format(insert_count_guest))

        # Insert Party data
        insert_count_party = Party.objects.from_csv(
            'data/test_party_data.csv',
            static_mapping = {
                'is_invited': True,
                'is_attending': False,
                'rehearsal_dinner': False,
            })
        print("{} test party records inserted".format(insert_count_party))