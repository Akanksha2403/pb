# Generated by Django 3.2.6 on 2021-08-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_auto_20210811_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ml',
            name='code',
        ),
        migrations.RemoveField(
            model_name='web',
            name='code',
        ),
        migrations.AddField(
            model_name='ml',
            name='img',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
        migrations.AddField(
            model_name='web',
            name='img',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
    ]
