# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-25 17:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('francais', '0011_submitdoc_stud_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submitdoc',
            old_name='date',
            new_name='created_on',
        ),
    ]