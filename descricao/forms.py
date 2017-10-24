from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	apartamento = forms.IntegerField()
	condominio = forms.CharField(max_length=150)
	liberacao = forms.CharField(max_length=200)
	data_liberacao = forms.DateField()
	nome_operador = forms.CharField(max_length=200)
	central = forms.CharField(max_length=200)
	descricao = forms.CharField(max_length=300)

	class Meta:
		model = Post
		fields = ['apartamento','condominio', 'liberacao', 'data_liberacao', 'nome_operador', 'central', 'descricao']