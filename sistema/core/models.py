# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Fornecedor(models.Model):

	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)
	nome = models.CharField(u'Razão Social',max_length=100, unique=True)
	cidade = models.CharField(u'Cidade',max_length=100)
	fone = models.CharField(u'Telefone',max_length=20)
	cnpj_cpf = models.CharField(u'CNPJ ou CPF',max_length=50, unique=True)
	email = models.CharField(u'E-Mail',max_length=200)
	slug = models.SlugField()

	def __str__(self):
		return self.nome


UNIDADE_MEDIDA = (
	('UN', 'UN'),
    ('KG', 'KG'),
    ('L', 'L'),
    ('CX', 'CX'),

)


class Categoria(models.Model):
	nome = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)
	def __str__(self):
		return self.nome


class Produto(models.Model):

	nome = models.CharField(max_length=100,unique=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	codigo_barras = models.IntegerField(u'Código de Barras',)
	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)
	quantidade = models.CharField(max_length=100)
	unidade_medida = models.CharField(choices=UNIDADE_MEDIDA, max_length=10, blank=True, null=True)
	peso = models.FloatField(blank=True, null=True)
	valor_compra = models.DecimalField(u'Valor da compra por unidade', max_digits=5, decimal_places=2)
	valor_venda = models.DecimalField(u'Valor de venda por unidade', max_digits=5, decimal_places=2)
	fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100,)

	def __str__(self):
		return self.nome



class Cliente(models.Model):

	nome = models.CharField(u'Nome',max_length=100,unique=True)
	foto = models.ImageField(u'Foto',upload_to = '', default = 'cliente_default.png')
	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)

	cpf_cnpj = models.CharField(u'CNPJ ou CPF',max_length=50)

	cidade = models.CharField(u'Cidade',max_length=50, blank=True, null=True)
	endereco = models.CharField(u'Endereço',max_length=200, blank=True, null=True)
	fone = models.CharField(u'Fone',max_length=20, blank=True, null=True)
	email = models.EmailField('E-Mail',max_length=200, blank=True, null=True)
	slug = models.SlugField(max_length=100,)


	def __str__(self):
		return self.nome

