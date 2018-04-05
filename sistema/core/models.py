# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Ibge(models.Model):

	codigo_estado = models.IntegerField('Código do Estado',)
	codigo_municipal = models.IntegerField('Código do Município',)
	pais = models.CharField(u'País', max_length=20)
	uf = models.CharField(u'UF', max_length=2)

	def __str__(self):
		return self.pais

class Fornecedor(models.Model):

	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)

	nome_razao_social = models.CharField(u'Razão Social',max_length=100, unique=True, blank=True, null=True)
	nome_fantasia = models.CharField(u'Nome', unique=True, max_length=200)
	cpf = models.IntegerField(u'CPF', unique=True, blank=True, null=True)
	cnpj = models.IntegerField(u'CNPJ', unique=True, blank=True, null=True)
	inscricao_estadual = models.IntegerField(u'Inscrição estadual', blank=True, null=True)
	rua_endereco = models.CharField(u'Rua',max_length=100, blank=True, null=True )
	numero_endereco = models.CharField(u'Número', max_length=20, blank=True, null=True )
	complemento_end = models.CharField(u'Complemento', max_length=200, blank=True, null=True )
	bairro = models.CharField(u'Bairro',max_length=100, blank=True, null=True )
	cidade = models.CharField(u'Cidade',max_length=100, blank=True, null=True )
	codigo_ibge_cidade = models.ForeignKey(Ibge, blank=True, null=True)
	cep = models.IntegerField(u'CEP', blank=True, null=True)
	email = models.EmailField(u'Email', max_length=100, blank=True, null=True)
	telefone = models.CharField(u'Telefone', max_length=20, blank=True, null=True)

	pessoa_juridica = models.BooleanField(default=True)
	ativo = models.BooleanField(default=True)

	slug = models.SlugField()

	def __str__(self):
		return self.nome_fantasia



class Tributacao(models.Model):
	descricao = models.TextField(u'Descrição', unique=True)
	csosn = models.IntegerField(u'CSOSN',)
	cfop_interno = models.IntegerField(u'CFOP Interno',)
	cfop_externo = models.IntegerField(u'CFOP Externo',)
	def __str__(self):
		return self.descricao


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


	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)
	imagem = models.ImageField(u'Imagem do Produto',upload_to = '', default = 'produto_default.png')
	codigo_de_barras = models.IntegerField(u'Código de Barras',unique=True)
	descricao = models.TextField(u'Descrição do Produto',unique=True)
	valor_compra = models.DecimalField(u'Valor da compra por unidade', max_digits=5, decimal_places=2)
	valor_venda = models.DecimalField(u'Valor de venda por unidade', max_digits=5, decimal_places=2)
	ncm = models.IntegerField(u'NCM',)
	tributacao = models.ForeignKey(Tributacao,on_delete=models.CASCADE)
	fornecedor = models.ForeignKey(Fornecedor,on_delete=models.CASCADE)
	unidade = models.IntegerField(u'Unidade',default=0)

	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

	slug = models.SlugField(max_length=100,)

	def __str__(self):
		return self.descricao


class Cliente(models.Model):

	foto = models.ImageField(u'Foto',upload_to = '', default = 'cliente_default.png')
	pessoa_juridica = models.BooleanField(u'Pessoa Jurídica', default=True)
	nome_fantasia = models.CharField(u'Nome',max_length=100,unique=True)
	razao_social = models.CharField(u'Razão Social',max_length=100,unique=True,  blank=True, null=True)
	cnpj = models.CharField(u'CNPJ',max_length=50,blank=True, null=True)
	cpf = models.CharField(u'CPF',max_length=50,blank=True, null=True)
	rua_endereco = models.CharField(u'Rua',max_length=200, blank=True, null=True)
	numero_endereco = models.CharField(u'Número',max_length=10, blank=True, null=True)
	complemento_endereco = models.CharField(u'Complemento',max_length=100, blank=True, null=True)
	bairro = models.CharField(u'Bairro',max_length=50, blank=True, null=True)
	cidade = models.CharField(u'Cidade',max_length=50, blank=True, null=True)
	codigo_ibge_cidade = models.ForeignKey(Ibge, null=True, blank=True)
	cep = models.IntegerField(u'CEP',blank=True, null=True)

	codigo_pais = models.IntegerField(u'Código do País', default=1058,  blank=True, null=True)
	nome_pais = models.CharField(u'País', default='Brasil', max_length=20,  blank=True, null=True)
	inscricao_estadual = models.IntegerField(u'Inscrição Estadual', blank=True, null=True)

	fone = models.CharField(u'Fone',max_length=20, blank=True, null=True)
	email = models.EmailField('E-Mail',max_length=200, blank=True, null=True)

	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)

	slug = models.SlugField(max_length=100,)

	def __str__(self):
		return self.nome_fantasia

FORMA_DE_PAGAMENTO = (
		(0,'À Vista'),
		(1,'Cartão'),
		(2,'Fiado'),
	)


STATUS_DA_VENDA = (
		(0,'Pedido'),
		(1,'Vendido'),

	)

class CabecalhoNfe(models.Model):

	status_venda = models.CharField(u'Status da Venda', max_length=20, choices=STATUS_DA_VENDA, default=0)

	data_venda = models.DateField(u'Data da venda',)
	cliente = models.ForeignKey(Cliente)
	valot_total =  models.DecimalField(u'Valor Total', max_digits=5, decimal_places=2, null=True, blank=True)
	desconto_acrescimo =  models.DecimalField(u'Desconto ou Acréscimo', max_digits=5, decimal_places=2, default=0)
	forma_de_pagamento = models.IntegerField(u'Forma de Pagamento', choices=FORMA_DE_PAGAMENTO)

	numero_nfe = models.IntegerField(u'Numero da Nota Fiscal Eletrónica',null=True, blank=True, unique=True)
	serie_nfe = models.IntegerField(u'Série NFe',)
	protocolo_autorizacao_nfe = models.IntegerField(u'Protocolo de Autorização',null=True, blank=True)
	chave_nfe = models.IntegerField(u'Chave de Autorização',null=True, blank=True)
	status_nfe = models.CharField(u'Status da NFe',null=True, blank=True, max_length=50)
	observacao_venda = models.TextField(u'Observações',null=True, blank=True)

	criado_em = models.DateTimeField(auto_now_add=True)
	editado_em = models.DateTimeField(auto_now=True)
	criado_por = models.CharField(max_length=100)
	editado_por = models.CharField(max_length=100, blank=True, null=True)

	slug = models.SlugField(max_length=100,)

	def __str__(self):
		return self.cliente.nome_fantasia


class ItensNfe(models.Model):
	criado_em = models.DateTimeField(auto_now_add=True)
	criado_por = models.CharField(max_length=100)
	produto = models.ForeignKey(Produto)
	quantidade_venda = models.IntegerField()

	def __str__(self):
		return self.produto.descricao
