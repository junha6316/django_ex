# Generated by Django 3.2.5 on 2021-07-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlog',
            name='is_cancel',
            field=models.BooleanField(default=False),
        ),
    ]
