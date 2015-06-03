# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='course_taken',
            field=models.CharField(default=b'n/a', max_length=8),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='review',
            name='date_published',
            field=models.DateTimeField(default=datetime.date(2014, 11, 18), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
