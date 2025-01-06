from django.core.management.base import BaseCommand
from tasks.models import Task
import time
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'Print all tasks in the database one by one every 10 seconds'

    def handle(self, *args, **kwargs):
        tasks = Task.objects.all()  # Retrieve all tasks
        for task in tasks:
            # Instead of print(), we could log the tasks to a file or database
            self.stdout.write(f"Task: {task.title}, Duration: {task.duration}, Created at: {task.created_at}")
            
            # Wait for 10 seconds before displaying the next task
            time.sleep(10)
