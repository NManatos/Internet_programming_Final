# Generated by Django 4.0.5 on 2022-07-16 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landingPage', '0009_remove_data_user_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='first',
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='last',
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookingUser', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bookingEvent', to='landingPage.event'),
        ),
        migrations.RemoveField(
            model_name='data_user',
            name='event',
        ),
        migrations.AddField(
            model_name='data_user',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='landingPage.event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=64),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_value', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ratingEvent', to='landingPage.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ratingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
