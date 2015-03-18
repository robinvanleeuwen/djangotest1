# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150316_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone1',
            field=models.CharField(default=b'', max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='phone2',
            field=models.CharField(default=b'', max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='phone1',
            field=models.CharField(default=b'', max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipient',
            name='phone2',
            field=models.CharField(default=b'', max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name1',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='name2',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='zip',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='email',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='name1',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='name2',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='street',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='zip',
            field=models.CharField(default=b'', max_length=255, null=True),
            preserve_default=True,
        ),
    ]
