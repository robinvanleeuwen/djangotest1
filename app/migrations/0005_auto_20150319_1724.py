# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150319_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name1', models.CharField(max_length=255)),
                ('name2', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('client_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255)),
                ('langauge', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.ForeignKey(to='app.Country', unique=True),
            preserve_default=True,
        ),
    ]
