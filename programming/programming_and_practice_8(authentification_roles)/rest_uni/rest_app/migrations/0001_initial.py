# Generated by Django 4.1.2 on 2022-10-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Containers',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=8)),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('departure_date', models.CharField(max_length=10)),
                ('arrival_date', models.CharField(max_length=10)),
                ('amount_of_items', models.PositiveIntegerField()),
            ],
        ),
    ]
