# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

# Register your models here.
from pagedown.widgets import AdminPagedownWidget

from models import Article

class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }



admin.site.register(Article, ArticleAdmin)