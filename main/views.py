from unidecode import unidecode
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from main.models import Post
from main.forms import NewPostForm, PartialNewPostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


class RegistrationFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegistrationFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect("/")


class NewPostView(FormView):
    form_class = PartialNewPostForm
    template_name = 'newpost.html'
    success_url = '/'

    def form_valid(self, form):
        form = PartialNewPostForm(self.request.POST)
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = unidecode(post.title)
        post.slug = slugify(post.slug)
        post.save()
        self.success_url = "/post/" + post.slug
        return super(NewPostView, self).form_valid(form)

    def get_success_url(self):
        return self.success_url


class PostView(View):
    template_name = 'postview.html'

    def get(self, request, post_title):
        post = Post.objects.filter(slug=post_title)[0]
        return render(request, "postview.html", {"post": post})
