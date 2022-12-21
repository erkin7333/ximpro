# Generated by Django 4.0.4 on 2022-05-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_services_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeimages',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='homeimages',
            name='video_background',
        ),
        migrations.AddField(
            model_name='homeimages',
            name='video',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Video'),
        ),
    ]
