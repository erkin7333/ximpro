# Generated by Django 3.2 on 2022-08-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0058_alter_membershiptranslation_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='adress',
        ),
        migrations.AddField(
            model_name='membershiptranslation',
            name='adress',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Adress'),
        ),
    ]
