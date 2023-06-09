# Generated by Django 4.2 on 2023-05-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_airlinecompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_id', models.CharField(max_length=100)),
                ('seat_id', models.IntegerField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('customer_id', models.IntegerField(max_length=500)),
                ('phone', models.IntegerField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FindFlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=100)),
                ('arrival', models.CharField(max_length=100)),
            ],
        ),
    ]
