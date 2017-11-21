# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Condominio(models.Model):
	ramal = models.IntegerField()
	nome = models.CharField(max_length=220)
	observacao = models.TextField(max_length=320)

	def __str__(self):
		return self.nome

class Usuario(models.Model):
	nome = models.CharField(max_length=200)
	sobrenome = models.CharField(max_length=200)
	email = models.EmailField()
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.nome

class Central(models.Model):
	nome = models.CharField(max_length=220)
	ramal_interno = models.IntegerField()
	supervisor = models.ForeignKey(Usuario)

	def __str__(self):
		return self.nome

class StatusLiberacao(models.Model):
	status = models.CharField(max_length=120)

	def __str__(self):
		return self.status

class Post(models.Model):
	apartamento = models.IntegerField()
	condominio = models.ManyToManyField(Condominio)
	liberacao = models.ForeignKey(StatusLiberacao)
	data_liberacao = models.DateField()
	nome_operador = models.ForeignKey(Usuario)
	central = models.ForeignKey(Central)
	descricao = models.TextField(max_length=300)

	def __str__(self):
		return self.liberacao