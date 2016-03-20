# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0003_auto_20160320_0945'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([('object_id', 'content_type', 'creator')]),
        ),
    ]
