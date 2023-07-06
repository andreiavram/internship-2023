from django.core.management import BaseCommand

from todo.tasks import create_task


class Command(BaseCommand):
    help = "Run my command"

    def handle(self, *args, **options):
        for i in range(1, 10):
            self.stdout.write("Created Task")
            create_task.apply_async(args=(), queue="yeti")
