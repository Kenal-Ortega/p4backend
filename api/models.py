from django.db import models
from authentication.models import User


class Todo(models.Model):

    class Meta:
        verbose_name_plural = 'todo'

    task = models.CharField(max_length=255, default=None)
    objective = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task


class Achievements(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, related_name='todo', on_delete=models.CASCADE)

    objective = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.todo.task
