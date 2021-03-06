# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descricao', '0009_auto_20171104_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Central',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Central', models.CharField(max_length=220)),
                ('ramal_interno', models.IntegerField()),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descricao.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ramal', models.IntegerField()),
                ('Nome', models.CharField(max_length=220)),
                ('Observações', models.TextField(max_length=320)),
            ],
        ),
        migrations.DeleteModel(
            name='Delete',
        ),
        migrations.RemoveField(
            model_name='post',
            name='condominio',
        ),
        migrations.AddField(
            model_name='post',
            name='condominio',
            field=models.ManyToManyField(to='descricao.Condominio'),
        ),
    ]
