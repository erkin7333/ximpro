# Generated by Django 3.2 on 2022-07-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_alter_abouttranslation_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Slug'),
        ),
    ]
