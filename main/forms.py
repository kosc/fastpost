from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from captcha.fields import CaptchaField
from main.models import Post, Comment


class NewPostForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['created_at']


class PartialNewPostForm(ModelForm):
    tags_field = CharField()

    class Meta:
        model = Post
        fields = ['title', 'content']


class NewCommentForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        exclude = ['author', 'post']


class RegistrationForm(UserCreationForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ["username", "email"]
