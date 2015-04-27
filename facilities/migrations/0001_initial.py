# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to='facilities/icons/', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
    ]
