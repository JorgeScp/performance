# Generated by Django 3.0.6 on 2020-06-29 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='none', max_length=100)),
                ('identification', models.IntegerField(blank=True, null=True)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, default='None', max_length=50, null=True)),
                ('doi', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
                ('jobname', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.JobName')),
            ],
        ),
    ]