# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.CharField(max_length=100)),
                ('stdout', models.TextField(blank=True)),
                ('stderr', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exc_type', models.CharField(max_length=200, null=True, blank=True)),
                ('exc_value', models.TextField(null=True, blank=True)),
                ('exc_traceback', models.TextField(null=True, blank=True)),
                ('duration', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
