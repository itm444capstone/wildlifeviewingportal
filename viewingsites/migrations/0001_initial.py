# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
        ('animals', '0001_initial'),
        ('facilities', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewSite',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('ada', models.BooleanField(help_text='Is the site ADA compliant?', verbose_name='American Disabilities Act Compliant?', default=False)),
                ('fee', models.BooleanField(help_text='Does the site have a fee?', verbose_name='Entry Fee?', default=False)),
                ('publish', models.BooleanField(help_text='Do you want to publish the site?', verbose_name='Publish?', default=False)),
                ('owner', models.CharField(null=True, blank=True, max_length=100)),
                ('owner_link', models.CharField(help_text='Link to viewing site website', null=True, blank=True, max_length=500, verbose_name='Viewing Site Website')),
                ('alerts', models.ManyToManyField(blank=True, to='alerts.Alert')),
                ('animals', models.ManyToManyField(blank=True, to='animals.Animal')),
                ('facilities', models.ManyToManyField(blank=True, to='facilities.Facility')),
                ('photos', models.ManyToManyField(blank=True, to='photos.Photo')),
            ],
            options={
                'verbose_name': 'Viewing Site',
                'verbose_name_plural': 'Viewing Sites',
            },
        ),
    ]
