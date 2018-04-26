# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20180320_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='downvote',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='upvote',
        ),
        migrations.AddField(
            model_name='picture',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picture',
            name='tag',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.FileField(upload_to=b''),
        ),
    ]
