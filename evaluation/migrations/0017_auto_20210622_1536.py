# Generated by Django 3.0.6 on 2021-06-22 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0016_auto_20210622_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 20, 36, 38, 551203, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='apptest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 20, 36, 38, 551203, tzinfo=utc)),
        ),
    ]
