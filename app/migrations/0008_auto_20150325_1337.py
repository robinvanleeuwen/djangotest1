# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150320_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.ForeignKey(to='app.Country'),
            preserve_default=True,
        ),
    ]
