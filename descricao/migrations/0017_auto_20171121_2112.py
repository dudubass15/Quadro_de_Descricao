# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descricao', '0016_auto_20171120_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusLiberacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='central',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Usuario'),
        ),
        migrations.AlterField(
            model_name='post',
            name='liberacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.StatusLiberacao'),
        ),
        migrations.AlterField(
            model_name='post',
            name='nome_operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Usuario'),
        ),
    ]
