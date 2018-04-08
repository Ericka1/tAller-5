# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('sucursal', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id_vendedor', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=1)),
                ('sucursal', models.ForeignKey(blank=True, to='index.Sucursal', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.IntegerField(serialize=False, primary_key=True)),
                ('cliente', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('producto', models.CharField(max_length=80)),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('sucursal', models.ForeignKey(blank=True, to='index.Sucursal', null=True)),
                ('vendedor', models.ForeignKey(blank=True, to='index.Vendedor', null=True)),
            ],
        ),
    ]
