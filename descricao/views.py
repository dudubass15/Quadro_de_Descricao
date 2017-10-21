# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import PostForm


def index(request):
    return render(request, 'index.html', {})

def adicionar(request):
	if request.method == "POST":
	    form = PostForm(request.POST)
	else:
	    form = PostForm()

	form = PostForm()
    	return render(request, 'inserir.html', {'form': form})