# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCodes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iso_3116_1_alpha2', models.CharField(default=b'', max_length=2, unique=True, null=True)),
                ('iso_3116_1_alpha3', models.CharField(default=b'', max_length=3, null=True)),
                ('iso_3116_1_num', models.IntegerField(default=0, null=True)),
                ('eu_country', models.BooleanField(default=False)),
                ('country_desc', models.IntegerField(default=0, null=True)),
                ('language_code', models.CharField(default=b'', max_length=3, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name1', models.CharField(max_length=255)),
                ('name2', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('customerNumber', models.IntegerField(unique=True, db_index=True)),
                ('country_desc', models.ForeignKey(to='app.CountryCodes', unique=True)),
            ],
            options={
                'ordering': ['name1'],
                'abstract': False,
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name1', models.CharField(max_length=255)),
                ('name2', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('recipientNumber', models.IntegerField(unique=True, db_index=True)),
                ('country_desc', models.ForeignKey(to='app.CountryCodes', unique=True)),
            ],
            options={
                'ordering': ['name1'],
                'abstract': False,
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='recipient',
            index_together=set([('name1', 'name2')]),
        ),
        migrations.AlterIndexTogether(
            name='customer',
            index_together=set([('name1', 'name2')]),
        ),
    ]
