# Generated by Django 3.1.6 on 2021-04-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventManager', '0002_postevent_event_foodqty'),
    ]

    operations = [
        migrations.AddField(
            model_name='postevent',
            name='event_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='postevent',
            name='event_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
