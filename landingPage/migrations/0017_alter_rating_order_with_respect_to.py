# Generated by Django 4.0.5 on 2022-07-18 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0016_alter_event_date'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='rating',
            order_with_respect_to='rating_value',
        ),
    ]
