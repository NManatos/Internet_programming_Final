# Generated by Django 4.0.5 on 2022-07-18 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0021_rename_ratingadmin_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
