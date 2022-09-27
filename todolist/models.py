from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TodoListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    isFinished = models.BooleanField(default=False)