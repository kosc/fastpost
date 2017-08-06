from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms import ModelForm

from main.models import Post, Comment


class NewPostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['created_at']


class PartialNewPostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['created_at', 'author', 'slug', 'short_content']


class NewCommentForm(ModelForm):

    class Meta:
        model = Comment
        exclude = ['author', 'post']
