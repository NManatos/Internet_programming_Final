# Generated by Django 4.0.5 on 2022-07-19 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0032_alter_userlabel_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
