from django.contrib import admin

from sherlock.models import Profile, About

admin.site.register([Profile, About])