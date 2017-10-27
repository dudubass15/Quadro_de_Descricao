# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

class PostAdmin(ModelAdmin):
    list_display = ('apartamento', 'condominio', 'descricao', 'liberacao', 'central', 'nome_operador')

admin.site.register(Post, PostAdmin)