from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    picture = models.ImageField(upload_to="pics")


class Post(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=255)
    content = models.TextField()
    pictures = models.ManyToManyField(Picture)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.OneToOneField(to=User)


class Comment(models.Model):

    def __str__(self):
        return self.text[0:20]

    text = models.TextField()
    author = models.OneToOneField(to=User)
