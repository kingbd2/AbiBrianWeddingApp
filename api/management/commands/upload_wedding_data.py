from api.models import Guest, Party, Location, Event
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)

        # Insert Guest data
        insert_count_guest = Guest.objects.from_csv(
            'data/guest_data.csv',
            )
        print("{} guest records inserted".format(insert_count_guest))

        # Insert Party data
        insert_count_party = Party.objects.from_csv(
            'data/party_data.csv',
            static_mapping={
                'is_invited': True,
                'is_attending': False,
                'rehearsal_dinner': False,
            })
        print("{} party records inserted".format(insert_count_party))

        # Insert Location data
        insert_count_location = Location.objects.from_csv(
            'data/location_data.csv')
        print("{} location records inserted".format(insert_count_location))

        # Insert Event data 
        insert_count_event = Event.objects.from_csv(
            'data/event_data.csv')
        print("{} event records inserted".format(insert_count_event))
