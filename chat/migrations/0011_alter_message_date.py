# Generated by Django 3.2.6 on 2021-08-18 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 18, 16, 18, 56, 110767)),
        ),
    ]
