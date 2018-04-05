# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Fornecedor, Produto, Categoria, Cliente, CabecalhoNfe
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from .forms import CabecalhoNfeForm, FornecedorForm, ProdutoForm, CategoriaForm, ClienteForm, FornecedorPessoaJuridicaForm, FornecedorPessoaFisicaForm, ClientePessoaJuridicaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from decimal import Decimal
import re

@login_required(login_url="/login")
def home(request):
	#Retorna para a Tela Principal do Sistema
	return render(request, 'core/home.html')

#####################################################################
##################### Venda #########################################
#####################################################################

@login_required(login_url="/login")
def cabecalho_nfe(request):
	form = CabecalhoNfeForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.numero_nfe)
			salvar.save()
			return redirect('itens_nfe', slug=salvar.slug)
		else:
			return render(request, 'core/venda/cabecalho_pedido.html', {'form':form})
	else:
		return render(request, 'core/venda/cabecalho_pedido.html', {'form':form})

@login_required(login_url="/login")
def itens_nfe(request, slug):
	cabecalho_nfe = get_object_or_404(CabecalhoNfe, slug=slug)
	return render(request, 'core/venda/itens_pedido.html', {'cabecalho_nfe':cabecalho_nfe})


#####################################################################
##################### Fornecedores ##################################
#####################################################################
# Listar Fornecedores
@login_required(login_url="/login")
def fornecedores(request):

	# Se u usuario clicar no botao de pesquisar
	if request.method == 'POST':
		# Variavel q recebe o texto informado na busca
		q = request.POST['q']
		lista_aux = Fornecedor.objects.filter(Q(nome__contains=q) | Q(cnpj_cpf=q) | Q(cidade__contains=q)  ).order_by('-id')
	else:
		lista_aux = Fornecedor.objects.all().order_by('-id').order_by('-id')

	paginator = Paginator(lista_aux, 25)
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		lista = paginator.page(1)
	except EmptyPage:
		lista = paginator.page(paginator.num_pages)
	context = {
		'lista':lista,
		}
	return render(request, 'core/fornecedor/listar.html', context)

#####################################################################
######### Fornecedores  Pessoa Juridica #############################
#####################################################################

@login_required(login_url="/login")
def editar_fornecedor_pessoa_juridica(request, slug):
    post = get_object_or_404(Fornecedor, slug=slug)
    if request.method == "POST":
        form = FornecedorPessoaJuridicaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_fornecedor_pessoa_juridica', slug=post.slug)
    else:
        form = FornecedorForm(instance=post)
    return render(request, 'core/fornecedor/editar.html', {'form': form})

#Criar Fornecedor Pessoa Juridica
@login_required(login_url="/login")
def criar_fornecedor_pessoa_juridica(request):
	form = FornecedorPessoaJuridicaForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.nome_fantasia)
			salvar.save()
			return redirect('fornecedores')
		else:
			return render(request, 'core/fornecedor/criar.html', {'form':form})
	else:
		return render(request, 'core/fornecedor/criar.html', {'form':form})


#####################################################################
######### Fornecedores  Pessoa Física ###############################
#####################################################################

#Criar Fornecedor Pessoa Juridica
@login_required(login_url="/login")
def criar_fornecedor_pessoa_fisica(request):
	form = FornecedorPessoaFisicaForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.nome_fantasia)
			salvar.save()
			return redirect('fornecedores')
		else:
			return render(request, 'core/fornecedor/criar_pessoa_fisica.html', {'form':form})
	else:
		return render(request, 'core/fornecedor/criar_pessoa_fisica.html', {'form':form})


@login_required(login_url="/login")
def editar_fornecedor_pessoa_fisica(request, slug):
    post = get_object_or_404(Fornecedor, slug=slug)
    if request.method == "POST":
        form = FornecedorPessoaFisicaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_fornecedor_pessoa_fisica', slug=post.slug)
    else:
        form = FornecedorPessoaFisicaForm(instance=post)
    return render(request, 'core/fornecedor/editar.html', {'form': form})

# Detalhe do Fornecedor
@login_required(login_url="/login")
def fornecedor_detalhe(request, slug):
	fornecedor =  get_object_or_404(Fornecedor, slug=slug)
	context = {
		'fornecedor':fornecedor,
	}
	return render(request, 'core/fornecedor/detalhe.html', context)

#Criar Fornecedor
@login_required(login_url="/login")
def criar_fornecedor(request):
	form = FornecedorForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.nome)
			salvar.save()
			return redirect('fornecedores')
		else:
			return render(request, 'core/fornecedor/criar.html', {'form':form})
	else:
		return render(request, 'core/fornecedor/criar.html', {'form':form})





@login_required(login_url="/login")
def remove_fornecedor(request, slug):
	fornecedor = get_object_or_404(Fornecedor, slug=slug)
	fornecedor.delete()
	return redirect('fornecedores')

@login_required(login_url="/login")
def editar_fornecedor(request, slug):
    post = get_object_or_404(Fornecedor, slug=slug)
    if request.method == "POST":
        form = FornecedorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_fornecedor', slug=post.slug)
    else:
        form = FornecedorForm(instance=post)
    return render(request, 'core/fornecedor/editar.html', {'form': form})



#####################################################################
#####################    Produtos  ##################################
#####################################################################
@login_required(login_url="/login")
def venda(request):
	return render(request, 'core/produto/venda.html')

@login_required(login_url="/login")
def produtos(request):

	# Se u usuario clicar no botao de pesquisar
	if request.method == 'POST':
		# Variavel q recebe o texto informado na busca
		q = request.POST['q']

		if q:
			lista_aux = Produto.objects.filter(Q(descricao__contains=q) ).order_by('-id')
		else:
			lista_aux = Produto.objects.all().order_by('-id')
	else:
		lista_aux = Produto.objects.all().order_by('-id')

	paginator = Paginator(lista_aux, 25)
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		lista = paginator.page(1)
	except EmptyPage:
		lista = paginator.page(paginator.num_pages)
	context = {
		'lista':lista,
		}
	return render(request, 'core/produto/listar.html', context)

@login_required(login_url="/login")
def detalhe_produto(request, slug):

	produto =  get_object_or_404(Produto, slug=slug)


	context = {

		'produto':produto,


	}

	return render(request, 'core/produto/detalhe.html', context)

@login_required(login_url="/login")
def criar_produto(request):
	form = ProdutoForm(request.POST, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.codigo_de_barras)
			salvar.save()
			return redirect('produtos')
		else:
			return render(request, 'core/produto/criar.html', {'form':form})
	else:
		return render(request, 'core/produto/criar.html', {'form':form})


@login_required(login_url="/login")
def editar_produto(request, slug):
    post = get_object_or_404(Produto, slug=slug)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_produto', slug=post.slug)
    else:
        form = ProdutoForm(instance=post)
    return render(request, 'core/produto/editar.html', {'form': form})


@login_required(login_url="/login")
def remove_produto(request, slug):
	produto = get_object_or_404(Produto, slug=slug)
	produto.delete()
	return redirect('produtos')


#####################################################################
#####################    Categorias  ################################
#####################################################################

@login_required(login_url="/login")
def categorias(request):

	# Se u usuario clicar no botao de pesquisar
	if request.method == 'POST':
		# Variavel q recebe o texto informado na busca
		q = request.POST['q']

		if q:
			lista_aux = Categoria.objects.filter(Q(nome__contains=q)).order_by('-id')
		else:
			lista_aux = Categoria.objects.all().order_by('-id')
	else:
		lista_aux = Categoria.objects.all().order_by('-id')

	paginator = Paginator(lista_aux, 25)
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		lista = paginator.page(1)
	except EmptyPage:
		lista = paginator.page(paginator.num_pages)
	context = {
		'lista':lista,
		}
	return render(request, 'core/categoria/listar.html', context)

@login_required(login_url="/login")
def criar_categoria(request):
	form = CategoriaForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.nome)
			salvar.save()
			return redirect('categorias')
		else:
			return render(request, 'core/categoria/criar.html', {'form':form})
	else:
		return render(request, 'core/categoria/criar.html', {'form':form})


@login_required(login_url="/login")
def remove_categoria(request, slug):
	categoria = get_object_or_404(Categoria, slug=slug)
	categoria.delete()
	return redirect('categorias')


@login_required(login_url="/login")
def editar_categoria(request, slug):
    post = get_object_or_404(Categoria, slug=slug)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_categoria', slug=post.slug)
    else:
        form = CategoriaForm(instance=post)
    return render(request, 'core/categoria/editar.html', {'form': form})




#####################################################################
#####################    CLIENTES  ##################################
#####################################################################

@login_required(login_url="/login")
def clientes(request):
	if request.method == 'POST':
		q = request.POST['q']

		if q:
			lista_aux = Cliente.objects.filter(Q(nome__contains=q) | Q(cpf_cnpj=q)).order_by('-id')
		else:
			lista_aux = Cliente.objects.all().order_by('-id')
	else:
		lista_aux = Cliente.objects.all().order_by('-id')

	paginator = Paginator(lista_aux, 25)
	page = request.GET.get('page')
	try:
		lista = paginator.page(page)
	except PageNotAnInteger:
		lista = paginator.page(1)
	except EmptyPage:
		lista = paginator.page(paginator.num_pages)
	context = {
		'lista':lista,
		}
	return render(request, 'core/cliente/listar.html', context)

@login_required(login_url="/login")
def detalhe_cliente(request, slug):
	cliente =  get_object_or_404(Cliente, slug=slug)
	context = {
		'cliente':cliente,
	}
	return render(request, 'core/cliente/detalhe.html', context)

@login_required(login_url="/login")
def criar_cliente(request):
	form = ClientePessoaJuridicaForm(request.POST, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			salvar = form.save(commit=False)
			salvar.criado_por = request.user
			salvar.slug = slugify(salvar.nome_fantasia)
			salvar.save()
			return redirect('clientes')
		else:
			return render(request, 'core/cliente/criar.html', {'form':form})
	else:
		return render(request, 'core/cliente/criar.html', {'form':form})


@login_required(login_url="/login")
def remove_cliente(request, slug):
	cliente = get_object_or_404(Cliente, slug=slug)
	messages.success(request, 'Removido com sucesso!')
	cliente.delete()
	return redirect('clientes')


@login_required(login_url="/login")
def editar_cliente(request, slug):
    post = get_object_or_404(Cliente, slug=slug)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.editado_por = request.user.username
            messages.success(request, 'Editado com sucesso!')
            post.save()
            return redirect('editar_cliente', slug=post.slug)
    else:
        form = ClienteForm(instance=post)
    return render(request, 'core/cliente/editar.html', {'form': form})
