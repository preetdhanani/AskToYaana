
from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class GeneratedText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record at {self.created_at}"

from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class GeneratedText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record at {self.created_at}"
