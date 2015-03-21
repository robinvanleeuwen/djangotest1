# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150319_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='phone1',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='phone2',
            field=models.CharField(default=b'', max_length=255),
            preserve_default=True,
        ),
    ]
