# models.py
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()  # Duration in minutes or any appropriate unit
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'myapp_task'  # Optional: Change the default table name

    def __str__(self):
        return self.title
