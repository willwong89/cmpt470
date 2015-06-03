# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0009_remove_course_meta_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meta_score',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=1),
            preserve_default=True,
        ),
    ]
