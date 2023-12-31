# Generated by Django 3.2.10 on 2023-06-19 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_newsdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='commentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('blog', models.IntegerField(blank=True, null=True)),
                ('Comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
