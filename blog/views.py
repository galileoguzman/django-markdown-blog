# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Article as Post

# Create your views here.
def index_blog(request):
	index_template = "app/blog.html"
	secondary_posts = Post.objects.all()
	
	return render(request,index_template, {
		'posts': secondary_posts,
	})


def detail_post(request, slug):

	post = get_object_or_404(Post, slug=slug)
	
	return render(request, 'app/detail.html', {
		'post': post
	})