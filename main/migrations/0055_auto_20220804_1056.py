# Generated by Django 3.2 on 2022-08-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_auto_20220802_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=250, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
        migrations.AddField(
            model_name='projects',
            name='completed_job',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Completed Job'),
        ),
        migrations.AddField(
            model_name='projects',
            name='know_how',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Know How'),
        ),
        migrations.AddField(
            model_name='projects',
            name='new_developments',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='New Developments'),
        ),
        migrations.AddField(
            model_name='projects',
            name='projects',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Projects'),
        ),
    ]