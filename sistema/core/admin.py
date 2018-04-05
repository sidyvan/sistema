# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Fornecedor, Produto, Cliente, Ibge, Tributacao, CabecalhoNfe

admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Ibge)
admin.site.register(Tributacao)
admin.site.register(CabecalhoNfe)
