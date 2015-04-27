# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewingsites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewsite',
            name='telephone',
            field=models.CharField(null=True, blank=True, max_length=10),
        ),
    ]
