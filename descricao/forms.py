from django import forms
from .models import Post_descricao

class PostForm(forms.Form):
	apartamento = forms.IntegerField()
	condominio = forms.CharField(label='Condominio', max_length=150)
	descricao = forms.CharField(label='Descricao', widget=forms.Textarea)
	liberacao = forms.CharField(max_length=200)
	data_liberacao = forms.DateField()
	nome_operador = forms.CharField(label='Operador', max_length=200)
	central = forms.CharField(max_length=200)