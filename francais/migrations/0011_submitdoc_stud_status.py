# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-25 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('francais', '0010_auto_20170225_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitdoc',
            name='Stud_status',
            field=models.CharField(choices=[('stu', 'Stu'), ('Pro', 'Pro')], default='stu', max_length=3),
        ),
    ]
