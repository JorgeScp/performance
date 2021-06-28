# Generated by Django 3.0.6 on 2021-06-22 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Department',
            new_name='Boss',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='department',
            new_name='boss',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Team'),
        ),
    ]
