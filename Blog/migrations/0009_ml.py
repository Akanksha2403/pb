# Generated by Django 3.2.6 on 2021-08-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_blogpost_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ml',
            fields=[
                ('ml_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=5000)),
                ('algo', models.CharField(default='', max_length=900000)),
                ('code', models.CharField(default='', max_length=7000000)),
            ],
        ),
    ]
