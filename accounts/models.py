from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Consultaion(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation = models.TextField()
    def __str__(self):
        return self.name
