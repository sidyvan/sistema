from django import forms
from core.models import Fornecedor, Produto, Categoria, Cliente
from django.forms import TextInput,Select, PasswordInput, Textarea
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'name':'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'name':'password'}),

        }


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome', 'cnpj_cpf','cidade', 'fone',  'email')


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('codigo_barras','nome','categoria', 'quantidade','unidade_medida', 'peso',  'valor_compra', 'valor_venda', 'fornecedor')


        widgets = {
         
            'unidade_medida': Select(attrs={'class': 'form-control', 'name':'unidade_medida', 'id':'unidade_medida', 'onselect':'visivelFunction()'}),
            'peso': TextInput(attrs={'class': 'form-control','type':'number', 'name':'peso', 'name':'peso', 'id':'peso'}),

        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome',)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'foto', 'cpf_cnpj', 'cidade', 'endereco', 'fone', 'email')
