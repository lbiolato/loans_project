# Generated by Django 3.2.7 on 2021-09-18 20:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loansrequest', '0003_auto_20210918_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='dni',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1000000), django.core.validators.MaxValueValidator(70000000)]),
        ),
        migrations.AlterField(
            model_name='loan',
            name='edad',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
