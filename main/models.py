from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import re


class Picture(models.Model):
    picture = models.ImageField(upload_to="pics")


class Post(models.Model):

    def __str__(self):
        return self.title

    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    pictures = models.ManyToManyField(Picture, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)


class Comment(models.Model):

    def __str__(self):
        return self.text[0:20]

    text = models.TextField()
    author = models.OneToOneField(to=User)
