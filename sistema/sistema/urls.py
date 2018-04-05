"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Rota para a Tele Principal
    url(r'^$', views.home, name='home'),


    #url(r'^login/$', auth_views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/usuario/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/login'}, name='logout'),

    ####################################################################################################
    #################################### VENDA ########################################################
    ####################################################################################################
    url(r'^cabecalho-nfe/$', views.cabecalho_nfe, name='cabecalho_nfe'),
    url(r'^itens-nfe/(?P<slug>[\w-]+)/$', views.itens_nfe , name='itens_nfe'),
    ####################################################################################################
    #################################### FORNECEDOR ####################################################
    ####################################################################################################
    url(r'^fornecedores/$', views.fornecedores, name='fornecedores'),
    url(r'^criar-fornecedor/$', views.criar_fornecedor, name='criar_fornecedor'),
    url(r'^criar-fornecedor-pessoa-juridicar/$', views.criar_fornecedor_pessoa_juridica, name='criar_fornecedor_pessoa_juridica'),
    url(r'^fornecedor-detalhe/(?P<slug>[\w-]+)/$', views.fornecedor_detalhe , name='fornecedor_detalhe'),
    url(r'^remove-fornecedor/(?P<slug>[\w-]+)/$', views.remove_fornecedor , name='remove_fornecedor'),
    url(r'^editar-fornecedor/(?P<slug>[\w-]+)/$', views.editar_fornecedor , name='editar_fornecedor'),

    url(r'^editar-fornecedor-pessoa-juridica/(?P<slug>[\w-]+)/$', views.editar_fornecedor_pessoa_juridica , name='editar_fornecedor_pessoa_juridica'),

    url(r'^editar-fornecedor-pessoa-fisica/(?P<slug>[\w-]+)/$', views.editar_fornecedor_pessoa_fisica , name='editar_fornecedor_pessoa_fisica'),
    url(r'^criar-fornecedor-pessoa-fisica/$', views.criar_fornecedor_pessoa_fisica, name='criar_fornecedor_pessoa_fisica'),

    ####################################################################################################
    ################################### PRODUTO ########################################################
    ####################################################################################################
    url(r'^produtos/$', views.produtos, name='produtos'),
    url(r'^venda/$', views.venda, name='venda'),
    url(r'^criar-produto/$', views.criar_produto, name='criar_produto'),
    url(r'^detalhe-produto/(?P<slug>[\w-]+)/$', views.detalhe_produto , name='detalhe_produto'),
    url(r'^editar-produto/(?P<slug>[\w-]+)/$', views.editar_produto , name='editar_produto'),
    url(r'^revove-produto/(?P<slug>[\w-]+)/$', views.remove_produto , name='remove_produto'),
    ####################################################################################################
    ################################### CATEGORA #######################################################
    ####################################################################################################
    url(r'^categorias/$', views.categorias, name='categorias'),
    url(r'^criar-categoria/$', views.criar_categoria, name='criar_categoria'),
    url(r'^remove-categoria/(?P<slug>[\w-]+)/$', views.remove_categoria , name='remove_categoria'),
    url(r'^editar-categoria/(?P<slug>[\w-]+)/$', views.editar_categoria , name='editar_categoria'),
    ####################################################################################################
    ################################### CLIENTE ########################################################
    ####################################################################################################
    url(r'^clientes/$', views.clientes, name='clientes'),
    url(r'^criar-cliente/$', views.criar_cliente, name='criar_cliente'),
    url(r'^remove-cliente/(?P<slug>[\w-]+)/$', views.remove_cliente , name='remove_cliente'),
    url(r'^detalhe-cliente/(?P<slug>[\w-]+)/$', views.detalhe_cliente , name='detalhe_cliente'),
    url(r'^editar-cliente/(?P<slug>[\w-]+)/$', views.editar_cliente , name='editar_cliente'),
    ####################################################################################################


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
