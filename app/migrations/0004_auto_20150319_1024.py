# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150317_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Published')),
                ('title', models.CharField(max_length=200)),
                ('instructions', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(related_name='ingredients', to='app.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='customer',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AlterIndexTogether(
            name='recipient',
            index_together=None,
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='country',
        ),
        migrations.DeleteModel(
            name='CountryCodes',
        ),
        migrations.DeleteModel(
            name='Recipient',
        ),
    ]
