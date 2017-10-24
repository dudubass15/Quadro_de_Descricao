from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['apartamento','condominio', 'liberacao', 'data_liberacao', 'nome_operador', 'central', 'descricao']