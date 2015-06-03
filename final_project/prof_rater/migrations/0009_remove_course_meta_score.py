# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0008_auto_20141118_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='meta_score',
        ),
    ]
