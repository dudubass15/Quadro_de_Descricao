from django import forms
from .models import Post, Usuario, Delete

Centrais = (
    ('MI5', 'MI5'),
    ('Mossad', 'Mossad'),
)

Liberacao = (
	('Liberado', 'Liberado'),
	('A Liberar', 'A Liberar'),
	('Nao Liberado', 'Nao Liberado'),
)

class PostForm(forms.ModelForm):
	apartamento = forms.IntegerField()
	condominio = forms.CharField(max_length=150)
	liberacao = forms.ChoiceField(Liberacao)
	data_liberacao = forms.DateField()
	nome_operador = forms.CharField(max_length=200)
	central = forms.ChoiceField(Centrais)
	descricao = forms.TextInput()

	class Meta:
		model = Post
		fields = ['apartamento','condominio', 'liberacao', 'data_liberacao', 'nome_operador', 'central', 'descricao']

class DeleteForm(forms.ModelForm):
	apartamento = forms.IntegerField()
	condominio = forms.CharField(max_length=150)
	liberacao = forms.ChoiceField(Liberacao)
	data_liberacao = forms.DateField()
	nome_operador = forms.CharField(max_length=200)
	central = forms.ChoiceField(Centrais)
	descricao = forms.TextInput()

	class Meta:
		model = Delete
		fields = ['apartamento','condominio', 'liberacao', 'data_liberacao', 'nome_operador', 'central', 'descricao']

class UsuarioForm(forms.ModelForm):
	nome = forms.CharField(max_length=200)
	sobrenome = forms.CharField(max_length=200)
	email = forms.EmailField()
	password = forms.CharField(max_length=50, widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ['nome', 'sobrenome', 'email', 'password']