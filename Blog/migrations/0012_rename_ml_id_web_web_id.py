# Generated by Django 3.2.6 on 2021-08-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0011_auto_20210811_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='web',
            old_name='ml_id',
            new_name='web_id',
        ),
    ]