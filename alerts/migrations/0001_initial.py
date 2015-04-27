# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(null=True, max_length=50, blank=True)),
                ('level', models.IntegerField(choices=[(0, 'Notice'), (1, 'Warning'), (2, 'Danger')])),
                ('publish', models.BooleanField(verbose_name='Publish?', help_text='Publish this alert?', default=False)),
                ('publish_start_date', models.DateTimeField(verbose_name='Publish Start Date', help_text='Publish Start Date', auto_now_add=True)),
                ('publish_end_date', models.DateTimeField(verbose_name='Publish End Date', null=True, blank=True, help_text='Publish End Date')),
            ],
            options={
                'verbose_name': 'Alert',
                'verbose_name_plural': 'Alerts',
            },
        ),
    ]
