# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]
