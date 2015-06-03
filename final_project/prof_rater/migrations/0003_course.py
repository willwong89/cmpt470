# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_rater', '0002_auto_20141118_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(default=b'n/a', max_length=8)),
                ('title', models.CharField(max_length=50)),
                ('meta_score', models.DecimalField(max_digits=2, decimal_places=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
