# Generated by Django 4.0.5 on 2022-07-18 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0027_alter_item_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='value',
        ),
        migrations.AddField(
            model_name='item',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
