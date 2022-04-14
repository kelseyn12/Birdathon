# Generated by Django 4.0.2 on 2022-02-17 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_sighting_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeOfYear', models.CharField(choices=[('W', 'Winter'), ('SP', 'Spring'), ('SM', 'Summer'), ('F', 'Fall')], default='W', max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name='sighting',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='bird',
            name='seasons',
            field=models.ManyToManyField(to='main_app.Season'),
        ),
    ]