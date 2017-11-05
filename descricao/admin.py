# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, Usuario, Delete
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .forms import UsuarioForm

class PostAdmin(ModelAdmin):
    list_display = ('id','apartamento', 'condominio', 'descricao', 'liberacao', 'central', 'nome_operador')

class DeleteAdmin(ModelAdmin):
    list_display = ('apartamento', 'condominio', 'descricao', 'liberacao', 'central', 'nome_operador', 'data_exclusao')

class UsuarioAdmin(ModelAdmin):
	form = UsuarioForm
	list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Post, PostAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Delete, DeleteAdmin)