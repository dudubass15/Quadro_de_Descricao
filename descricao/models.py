# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Post_descricao(models.Model):
	
	apartamento = models.IntegerField()
	condominio = models.CharField(max_length=150)
	liberacao = models.CharField(max_length=200)
	data_liberacao = models.DateField()
	nome_operador = models.CharField(max_length=200)
	central = models.CharField(max_length=200)
	descricao = models.TextField(max_length=200)