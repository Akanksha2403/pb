# Generated by Django 3.2.6 on 2021-08-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_auto_20210812_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml',
            name='img',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
    ]