# Generated by Django 2.1.dev20180318005124 on 2018-04-03 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_picture_uploader_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]