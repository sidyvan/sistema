from django import forms
from core.models import Fornecedor, Produto, Categoria, Cliente, CabecalhoNfe
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


class CabecalhoNfeForm(forms.ModelForm):
    class Meta:
        model = CabecalhoNfe
        fields = ('data_venda', 'cliente','forma_de_pagamento', 'numero_nfe', 'serie_nfe', 'protocolo_autorizacao_nfe', 'chave_nfe', 'status_nfe', 'observacao_venda')
        widgets = {
            'data_venda': TextInput(attrs={'class': 'form-control', 'name':'data_venda', 'type':'date'}),


        }

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome_razao_social', 'nome_fantasia', 'cpf', 'cnpj', 'rua_endereco', 'numero_endereco', 'complemento_end', 'bairro', 'cidade', 'codigo_ibge_cidade', 'cep','inscricao_estadual', 'email','telefone')


class FornecedorPessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome_razao_social', 'nome_fantasia', 'cnpj', 'rua_endereco', 'numero_endereco', 'complemento_end', 'bairro', 'cidade', 'codigo_ibge_cidade', 'cep','inscricao_estadual', 'email','telefone')
        widgets = {
            'tefefone': TextInput(attrs={'class': 'form-control', 'name':'telefone', 'id':'telefone'}),
        }

class FornecedorPessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ('nome_fantasia', 'cpf', 'rua_endereco', 'numero_endereco', 'complemento_end', 'bairro', 'cidade', 'codigo_ibge_cidade', 'cep', 'email','telefone')
        widgets = {
            'tefefone': TextInput(attrs={'class': 'form-control', 'name':'telefone', 'id':'telefone'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('codigo_de_barras','imagem', 'categoria','descricao', 'valor_compra', 'valor_venda', 'ncm', 'tributacao', 'fornecedor', 'unidade')


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
        fields = ('__all__')

class ClientePessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_fantasia','razao_social','cnpj','rua_endereco','numero_endereco', 'complemento_endereco', 'bairro', 'cidade', 'codigo_ibge_cidade', 'cep', 'codigo_pais', 'nome_pais', 'inscricao_estadual', 'fone', 'email')
        #exclude = ('cpf','foto', 'pessoa_juridica', 'slug')

class ClientePessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('__all__')
        #exclude = ('pessoa_juridica', 'razao_social','cnpj', 'codigo_ibge_cidade', 'codigo_pais', 'nome_pais', 'slug')
