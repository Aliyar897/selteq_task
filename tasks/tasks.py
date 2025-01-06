from celery import shared_task
from datetime import datetime
from .models import Task  # Assuming you have a Task model with user ID and other details

@shared_task
def print_user_tasks():
    # Get tasks added by user with id 1
    tasks = Task.objects.filter(user_id=1)

    for task in tasks:
        print(f"Task Title: {task.title}")
        print(f"Duration: {task.duration}")
        print(f"Timestamp: {datetime.now()}")
