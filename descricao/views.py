# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect
from .forms import PostForm
from .models import Post


def index(request):
	post = Post.objects.all()

	return render(request, 'index.html', {'post': post})

def adicionar(request):
	if request.method == "POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	return HttpResponseRedirect('home') # Redireciona depois do POST
	else:
	    form = PostForm()

    	return render(request, 'inserir.html', {'form': form})