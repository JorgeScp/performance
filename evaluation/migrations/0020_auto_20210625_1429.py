# Generated by Django 3.0.6 on 2021-06-25 19:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0019_auto_20210625_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 25, 19, 29, 54, 892318, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='apptest',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 25, 19, 29, 54, 892318, tzinfo=utc)),
        ),
    ]