# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 18:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0002_auto_20171121_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacion',
            old_name='Pensum',
            new_name='pensum',
        ),
    ]