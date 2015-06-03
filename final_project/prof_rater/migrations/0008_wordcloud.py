# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        #('prof_rater', '0007_auto_20141118_1204'),
        ('prof_rater', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordCloud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase_one', models.CharField(default=b'', max_length=20)),
                ('phrase_two', models.CharField(default=b'', max_length=20)),
                ('phrase_three', models.CharField(default=b'', max_length=20)),
                ('professor', models.ForeignKey(to='prof_rater.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
