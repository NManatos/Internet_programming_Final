# Generated by Django 4.0.5 on 2022-07-18 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingPage', '0029_remove_item_id_remove_item_rating_remove_item_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]