# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=200, blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sites/images')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
            },
        ),
    ]
