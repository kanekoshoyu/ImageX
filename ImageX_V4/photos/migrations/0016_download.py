# Generated by Django 2.0.2 on 2018-04-26 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0015_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Picture')),
            ],
        ),
    ]