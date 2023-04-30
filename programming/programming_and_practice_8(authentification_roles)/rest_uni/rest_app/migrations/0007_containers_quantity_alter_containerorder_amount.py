# Generated by Django 4.1.3 on 2022-11-13 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0006_alter_containerorder_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='containers',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='containerorder',
            name='amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]