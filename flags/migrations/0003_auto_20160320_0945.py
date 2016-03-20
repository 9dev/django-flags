# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0002_approve'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='approve',
            unique_together=set([('object_id', 'content_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([('object_id', 'content_type')]),
        ),
    ]
