# Generated by Django 4.0.2 on 2022-02-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_sighting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='date',
            field=models.DateField(verbose_name='Sighting Date'),
        ),
    ]
