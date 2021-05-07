import csv
from CurrConverter.settings import CURRENCY_CSV
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from converter.models import CurrencyList


class Command(BaseCommand):
    """
    Seed will be a management command to seed your currency into
    your database
    """
    help = 'run in order to seed the currency tables.'

    def handle(self, *args, **kwargs):
        """
        Execution handler
        """
        try:
            list_of_currency = self.read_currency_csv()
            currency_objs = [
                CurrencyList(
                    currency=row['Currency'],
                    currency_code=row['CurrencyCode'],
                    created_by='INGEST'
                ) for row in list_of_currency
            ]
            CurrencyList.objects.bulk_create(currency_objs)
            self.stdout.write(self.style.SUCCESS(
                'Seeding of Currency table is completed succesfully')
            )
        except Exception as e:
            raise CommandError("Exception: {}".format(str(e)))

    def read_currency_csv(self):
        """
        Ready currency csv in order to save it
        """
        with open(CURRENCY_CSV, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            list_of_currency = list(reader)
            return list_of_currency
