# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post, Usuario, Condominio, Central, StatusLiberacao
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .forms import UsuarioForm

class PostAdmin(ModelAdmin):
    list_display = ('apartamento', 'liberacao', 'central', 'nome_operador')

class UsuarioAdmin(ModelAdmin):
	form = UsuarioForm
	list_display = ('nome', 'sobrenome', 'email')

class CondominioAdmin(ModelAdmin):
	list_display = ('ramal', 'nome', 'observacao')

class CentralAdmin(ModelAdmin):
	list_display = ('nome', 'ramal_interno', 'supervisor')

class StatusLiberacaoAdmin(ModelAdmin):
	list_display = ('status', 'status')

admin.site.register(Post, PostAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Central, CentralAdmin)
admin.site.register(StatusLiberacao, StatusLiberacaoAdmin)