# Generated by Django 2.0.2 on 2018-04-26 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0017_delete_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='download',
            name='member',
        ),
    ]
