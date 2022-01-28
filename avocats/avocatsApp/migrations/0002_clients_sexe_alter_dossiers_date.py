# Generated by Django 4.0 on 2022-01-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avocatsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='sexe',
            field=models.TextField(default=' ', verbose_name='Sexe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dossiers',
            name='date',
            field=models.DateTimeField(verbose_name='Date de reception'),
        ),
    ]