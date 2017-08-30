"""fastpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
import main.views

try:
    from .local_settings import ADMIN_URL
    if not ADMIN_URL: raise
except:
    ADMIN_URL = 'admin'

urlpatterns = [
    url(r'^{}/'.format(ADMIN_URL), admin.site.urls),

    url(r'^$', main.views.index),
    url(r'^register$', main.views.RegistrationFormView.as_view(), name='register'),
    url(r'^login$', main.views.LoginFormView.as_view(), name='login'),
    url(r'^logout$', main.views.LogoutView.as_view(), name='logout'),

    url(r'^newpost$', main.views.NewPostView.as_view(), name='newpost'),
    url(r'^editpost/(?P<post_id>\d+)$', main.views.EditPostView.as_view(), name='editpost'),

    url(r'^post/(?P<post_title>[a-zA-Z0-9\-_]+)', main.views.PostView.as_view(), name='viewpost'),

    url(r'^tag/(?P<tag_id>\w+)$', main.views.TagView.as_view(), name='tagsearch'),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
