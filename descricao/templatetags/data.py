from descricao.models import Post
from django.shortcuts import HttpResponse
from django import template

register = template.Library()

def FiltroData(data, FiltroData):
	resultado = Post.objects.all().filter(data_liberacao=data)
	return HttpResponse('index.html')