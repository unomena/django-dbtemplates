# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbtemplates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='publish_at',
            field=models.DateTimeField(db_index=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='template',
            name='retract_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='template',
            name='state',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'Published'), (1, b'Unpublished'), (2, b'Staged'), (3, b'Deleted')]),
        ),
    ]
