# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 01:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descricao', '0012_auto_20171120_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='central',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Usuario'),
        ),
        migrations.AlterField(
            model_name='post',
            name='central',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Central'),
        ),
        migrations.AlterField(
            model_name='post',
            name='nome_operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Usuario'),
        ),
    ]
