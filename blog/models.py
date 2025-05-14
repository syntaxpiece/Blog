from django.db import models

# Create your models here.


class Blog (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/image')
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title


class Project (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='project/image')
    link = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.title


class Quote (models.Model):
    author = models.CharField(max_length=50)
    quote = models.TextField()
    def __str__(self):
        return self.author

