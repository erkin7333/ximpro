# Generated by Django 4.0.4 on 2022-07-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_tables_tablestranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
