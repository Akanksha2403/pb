# Generated by Django 3.2.6 on 2021-08-12 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0020_auto_20210812_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='ai',
            name='file',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
