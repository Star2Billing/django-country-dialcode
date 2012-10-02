from django.core.management.base import BaseCommand
from django.core.management import call_command
import inspect
import os


class Command(BaseCommand):
    args = ' '
    help = "Load Dial Code\n"

    option_list = BaseCommand.option_list

    def handle(self, *args, **options):
        """
        Load country dialcode
        """
        script_directory = os.path.dirname(
            inspect.getfile(inspect.currentframe()))
        fixture_file = script_directory + \
            '/../../fixtures/country_dialcode.json'
        print "This fixture is going to be loaded : " + fixture_file
        call_command('loaddata', fixture_file)
