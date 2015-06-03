# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0005_auto_20141118_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date published'),
        ),
    ]
