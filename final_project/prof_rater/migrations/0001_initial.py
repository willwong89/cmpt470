# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('meta_score', models.DecimalField(max_digits=2, decimal_places=1)),
                ('department', models.ForeignKey(to='prof_rater.Department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.CharField(max_length=350)),
                ('interest_in_course', models.DecimalField(max_digits=2, decimal_places=1)),
                ('final_score', models.DecimalField(max_digits=2, decimal_places=1)),
                ('professor', models.ForeignKey(to='prof_rater.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
