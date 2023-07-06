from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Run my command"

    def handle(self, *args, **options):
        self.stdout.write("STDOUT")
        self.stderr.write("STDERR")
