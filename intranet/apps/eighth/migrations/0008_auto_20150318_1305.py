# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eighth', '0007_auto_20150318_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eighthscheduledactivity',
            name='comments',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
