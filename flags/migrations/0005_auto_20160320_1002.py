# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0004_auto_20160320_0947'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='flag',
            unique_together=set([]),
        ),
    ]
