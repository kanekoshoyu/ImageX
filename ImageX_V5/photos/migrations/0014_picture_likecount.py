# Generated by Django 2.0.2 on 2018-04-24 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0013_auto_20180409_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='likeCount',
            field=models.IntegerField(default=0),
        ),
    ]
