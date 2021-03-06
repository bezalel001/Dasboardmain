# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cpdashboard', '0003_auto_20160616_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('job_title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('slug', models.CharField(default='manager', max_length=10, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='department',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='initiatives',
        ),
        migrations.RemoveField(
            model_name='perspective',
            name='company',
        ),
        migrations.AddField(
            model_name='initiative',
            name='is_under_pressure',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='initiative',
            name='responsibility',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='perspective',
            name='slug',
            field=models.CharField(default='perspective', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='debit_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiatives', to='cpdashboard.Objective'),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='objective',
            name='perspective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objectives', to='cpdashboard.Perspective'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Designation',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]
