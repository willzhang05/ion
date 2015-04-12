# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='block',
            name='period',
        ),
        migrations.RemoveField(
            model_name='block',
            name='end',
        ),
        migrations.AddField(
            model_name='block',
            name='end',
            field=models.TimeField(verbose_name='Time'),
        ),
        migrations.RemoveField(
            model_name='block',
            name='start',
        ),
        migrations.AddField(
            model_name='block',
            name='start',
            field=models.TimeField(verbose_name='Time'),
        ),
        migrations.DeleteModel(
            name='Time',
        ),
    ]