# Generated by Django 4.0 on 2022-01-21 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avocatsApp', '0002_clients_sexe_alter_dossiers_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='sexe',
            field=models.CharField(max_length=50, verbose_name='Sexe'),
        ),
    ]
