# Generated by Django 4.0.5 on 2022-07-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0004_alter_event_coverimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='coverImg',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
