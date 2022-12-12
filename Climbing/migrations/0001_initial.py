# Generated by Django 4.1 on 2022-11-16 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClimbingSpots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City', models.CharField(max_length=20)),
                ('GeneralLocation', models.CharField(max_length=30)),
                ('Crag', models.CharField(max_length=30)),
                ('Wall', models.CharField(max_length=40)),
                ('Route', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=3000)),
                ('Difficulty', models.FloatField(default=0)),
                ('UserRatings', models.FloatField(default=0)),
                ('Comments', models.CharField(max_length=3000)),
            ],
        ),
    ]
