# Generated by Django 3.0.6 on 2021-07-14 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_auto_20210714_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_assign',
            name='done',
            field=models.CharField(blank=True, default='Asignado', max_length=100, null=True),
        ),
    ]
