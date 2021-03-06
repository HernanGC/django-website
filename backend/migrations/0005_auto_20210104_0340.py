# Generated by Django 3.1.4 on 2021-01-04 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210104_0340'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('long', models.IntegerField()),
                ('lat', models.IntegerField()),
                ('weather_main', models.CharField(max_length=30)),
                ('weather_description', models.CharField(max_length=30)),
                ('weather_icon', models.CharField(max_length=30)),
                ('temperature', models.IntegerField()),
                ('feels_like', models.IntegerField()),
                ('temp_min', models.IntegerField()),
                ('temp_max', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('visibility', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('wind_deg', models.IntegerField()),
                ('clouds', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.CharField(max_length=40),
        ),
    ]
