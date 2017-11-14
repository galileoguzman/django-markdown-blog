# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# DEPENDENCIES TO MAKE UNIQUE SLUG BY POST
from autoslug import AutoSlugField

# Create your models here.

class Article(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	slug = AutoSlugField(populate_from='name', unique_with='created_at', max_length=100, always_update=True, unique=True)

	@models.permalink
	def get_absolute_url(self):
		return 'blog:post', (self.slug,)

	def __str__(self):
		return '{}'.format(self.name)