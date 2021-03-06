# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 09:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0013_urlconfrevision'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityItemModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(default='Name', max_length=50)),
                ('location', models.CharField(default='Location', max_length=255)),
                ('datetime', models.DateTimeField()),
                ('links', models.TextField(default='Links')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
