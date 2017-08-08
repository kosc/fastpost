from unidecode import unidecode
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from main.models import Post, Comment, Tag
from main.forms import NewPostForm, PartialNewPostForm, NewCommentForm, \
                       RegistrationForm


def index(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'index.html', {'posts': posts})


class RegistrationFormView(FormView):
    form_class = RegistrationForm
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
        if self.request.POST['tags_field']:
            tags = self.request.POST['tags_field'].replace(', ', ',').split(',')
            for tag_name in tags:
                tag = Tag()
                tag.post = post
                tag.name = tag_name
                tag.save()
        self.success_url = "/post/" + post.slug
        return super(NewPostView, self).form_valid(form)

    def get_success_url(self):
        return self.success_url


class EditPostView(View):
    template_name = 'editpost.html'

    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = NewPostForm(instance=post)
        context = {
            "post": post,
            "form": form
        }
        return render(request, 'editpost.html', context)

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = NewPostForm(request.POST, instance=post)
        post = form.save()
        return redirect('/post/' + post.slug)


class PostView(View):
    template_name = 'postview.html'

    def get(self, request, post_title):
        post = Post.objects.filter(slug=post_title)[0]
        tags = Tag.objects.filter(post_id=post.id)
        comments = Comment.objects.filter(post_id=post.id)
        form = NewCommentForm()
        editable = False
        if post.author == request.user:
            editable = True
        context = {
            "post": post,
            "editable": editable,
            "comments": comments,
            "form": form,
            "tags": tags,
        }
        return render(request, "postview.html", context)

    def post(self, request, post_title):
        post = Post.objects.filter(slug=post_title)[0]
        comment = Comment()
        comment.post = post
        comment.text = request.POST['text']
        if isinstance(request.user, User):
            comment.author = request.user
            comment.save()
        else:
            form = NewCommentForm(request.POST)
            if form.is_valid():
                comment.save()
        return redirect('/post/' + post.slug)


class TagView(View):

    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        tags = Tag.objects.filter(name=tag.name)
        posts = []
        for tag in tags:
            posts.append(tag.post)
        context = {
            "posts": posts,
            "tag_name": tag.name,
        }
        return render(request, "tagsearch.html", context)
