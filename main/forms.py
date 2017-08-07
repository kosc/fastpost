from django.utils.translation import ugettext, ugettext_lazy as _
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField
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
    captcha = CaptchaField()

    class Meta:
        model = Comment
        exclude = ['author', 'post']


class RegistrationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ("username", "email")
