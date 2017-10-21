from django import forms
from .models import Post_descricao

class PostForm(forms.Form):
	apartamento = forms.IntegerField(
		widget=forms.NumberInput(attrs={'class':'form-control'})
	)
	condominio = forms.CharField(max_length=150, 
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	situacao_da_liberacao = forms.CharField(max_length=200, 
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	data_liberacao = forms.DateField(
		widget=forms.DateInput(attrs={'class':'form-control'})
	)
	operador = forms.CharField(max_length=200, 
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	central = forms.CharField(max_length=200, 
		widget=forms.TextInput(attrs={'class':'form-control'})
	)
	descricao = forms.CharField(max_length=200, 
		widget=forms.Textarea(attrs={'class':'form-control'})
	)

	class Meta:
		model = Post_descricao
		fields = ['apartamento','condominio', 'situacao_da_liberacao', 'data_liberacao', 'nome_operador', 'central', 'descricao']