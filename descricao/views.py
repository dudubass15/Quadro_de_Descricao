# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import PostForm
from descricao.models import Post

def index(request):
	post = Post.objects.all() #Aqui chama todos os objetos do banco e passa para o template (index)

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


def mossad(request):
	post = Post.objects.filter(central='Mossad')

	return render(request, 'mossad.html', {'post': post})

def adicionar_mossad(request):
	if request.method == "POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	return HttpResponseRedirect('mossad') # Redireciona depois do POST
	else:
	    form = PostForm()

	return render(request, 'inserir_mossad.html', {'form': form})

def mi5(request):
	post = Post.objects.filter(central='MI5')

	return render(request, 'mi5.html', {'post': post})

def adicionar_mi5(request):
	if request.method == "POST":
	    form = PostForm(request.POST)
	    if form.is_valid():
	    	form.save()
	    	return HttpResponseRedirect('mi5') # Redireciona depois do POST
	else:
	    form = PostForm()

	return render(request, 'inserir_mi5.html', {'form': form})


def search_mossad(request):
	busca = request.POST.get('Pesquisa')				#Recebe a requisão passada pelo form.
	if busca == '': 									#condição indicando que se busca for igual a vazio.
		busca = Post.objects.filter(central='Mossad') 	#Se a condiçao acima for True, filtra todos comparando Mossad.

		return HttpResponseRedirect('mossad') 			#retorna na página inicial mossad.html

	else: 												#Se não
		if busca == busca: 								#Se busca for igual a busca (informação passada no input do form)
			busca = Post.objects.filter(condominio__icontains=busca) #filtra o campo através do dado enviado pelo input.

			return render(request, 'mossad.html', {'post': busca}) #renderiza o filtro no template.

def search_mi5(request):
	busca = request.POST.get('Pesquisa')
	if busca == '':
		busca = Post.objects.filter(central='MI5')

		return HttpResponseRedirect('mi5')

	else:
		if busca == busca:
			busca = Post.objects.filter(condominio__icontains=busca)
			
			return render(request, 'mi5.html', {'post': busca})

def arquivar(request,pk):
	registro = Post.objects.get(id=pk)
	registro.delete()

	return redirect('mossad')