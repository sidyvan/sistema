# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo_de_barras',
            field=models.IntegerField(unique=True, verbose_name='Código de Barras'),
        ),
    ]
