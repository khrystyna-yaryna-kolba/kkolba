# Generated by Django 4.1.3 on 2022-11-12 20:54

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0004_userdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='containers',
            name='number',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_number', message='The invalid container number', regex='^[A-Z]{2}-[0-9]{5}$')]),
        ),
        migrations.CreateModel(
            name='ContainerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('container_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.containers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
