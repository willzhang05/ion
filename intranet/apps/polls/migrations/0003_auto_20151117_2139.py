# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151117_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['num']},
        ),
        migrations.AddField(
            model_name='answer',
            name='clear_vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(to='polls.Choice', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(default='STD', max_length=3, choices=[('STD', 'Standard'), ('ELC', 'Election'), ('APP', 'Approval'), ('SAP', 'Split approval'), ('FRE', 'Free response'), ('SRE', 'Short response'), ('STO', 'Standard other')]),
        ),
    ]
