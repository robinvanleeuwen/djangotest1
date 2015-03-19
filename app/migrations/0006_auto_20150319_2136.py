# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150319_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='langauge',
            new_name='language',
        ),
    ]
