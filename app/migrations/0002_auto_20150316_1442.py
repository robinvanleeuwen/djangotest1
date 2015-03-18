# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='country_desc',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='country_desc',
            new_name='country',
        ),
    ]
