# Generated by Django 4.0.5 on 2022-07-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0031_userlabel_delete_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlabel',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
