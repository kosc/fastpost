from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from transliterate import translit
from transliterate.exceptions import LanguageDetectionError
import re


class Picture(models.Model):
    picture = models.ImageField(upload_to="pics")


class Post(models.Model):

    def __str__(self):
        return self.title

    def generate_hru(self):
        """
        This function generate human-readable URL from post title
        If we can't delect language, assume that the language is English
        """
        hru = None
        try:
            hru = translit(self.title, reversed=True)
        except LanguageDetectionError:
            hru = self.title
        regex = re.compile("[^a-zA-Z0-9\ ]")
        hru = regex.sub("", hru)
        hru = hru.replace(" ", "-").lower()
        return hru

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
