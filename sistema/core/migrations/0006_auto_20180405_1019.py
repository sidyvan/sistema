# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-05 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180405_0839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='unidade',
            field=models.IntegerField(default=0, verbose_name='Unidade'),
        ),
    ]
