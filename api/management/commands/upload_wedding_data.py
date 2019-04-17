from api.models import CustomUser
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Since the CSV headers match the model fields,
        # you only need to provide the file's path (or a Python file object)
        insert_count_guest = CustomUser.objects.from_csv(
            'data/wedding_data.csv')
        # insert_count_party = Party.objects.from_csv(
        #     'data/Party.csv')
        print("{} guest records inserted".format(insert_count_guest))
        # print("{} party records inserted".format(insert_count_party))
