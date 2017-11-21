# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, Usuario, Condominio
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .forms import UsuarioForm

class PostAdmin(ModelAdmin):
    list_display = ('id','apartamento', 'descricao', 'liberacao', 'central', 'nome_operador')

class UsuarioAdmin(ModelAdmin):
	form = UsuarioForm
	list_display = ('nome', 'sobrenome', 'email')

class CondominioAdmin(ModelAdmin):
	list_display = ('ramal', 'nome', 'observacao')

admin.site.register(Post, PostAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Condominio, CondominioAdmin)