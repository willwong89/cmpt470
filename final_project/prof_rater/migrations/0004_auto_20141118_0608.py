# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0003_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department_name',
            new_name='name',
        ),
    ]
