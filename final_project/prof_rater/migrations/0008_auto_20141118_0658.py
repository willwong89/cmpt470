# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0007_auto_20141118_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='course_dept',
            new_name='course_subject',
        ),
    ]
