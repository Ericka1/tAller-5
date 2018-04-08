# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180403_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='cliente',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='direccion',
            field=models.CharField(max_length=500),
        ),
    ]
