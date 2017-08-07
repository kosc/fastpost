import re
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Picture(models.Model):
    picture = models.ImageField(upload_to="pics")


class Post(models.Model):

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        same_slug = True
        counter = 1
        while same_slug:
            same_slug = Post.objects.filter(slug=self.slug)
            if same_slug:
                self.slug += '_' + str(counter)
                counter += 1
            else:
                break
        self.short_content = strip_tags(self.content)[:100] + "..."
        super(Post, self).save(*args, **kwargs)

    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    short_content = models.CharField(max_length=255, blank=True)
    content = HTMLField()
    pictures = models.ManyToManyField(Picture, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)


class Comment(models.Model):

    def __str__(self):
        return self.text[0:20]

    post = models.ForeignKey(Post)
    text = models.TextField()
    author = models.ForeignKey(User, blank=True, null=True)


class Tag(models.Model):

    def __str__(self):
        return self.name

    post = models.ForeignKey(Post)
    name = models.CharField(max_length=255)
