# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_sucursal_vendedor_ventas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='sucursal',
        ),
    ]
