# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_remove_ventas_sucursal'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='ventas',
            name='total',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='ventas',
            name='valiva',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True),
        ),
        migrations.AddField(
            model_name='ventas',
            name='valor',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=3, blank=True),
        ),
    ]
