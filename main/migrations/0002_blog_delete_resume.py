# Generated by Django 4.0.4 on 2023-10-26 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('date', models.DateField(blank=True, default=datetime.datetime(2023, 10, 26, 11, 35, 38, 257793))),
                ('photo', models.ImageField(blank=True, upload_to='upload')),
                ('link', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
