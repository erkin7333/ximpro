# Generated by Django 3.2 on 2022-07-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Slug'),
        ),
    ]
