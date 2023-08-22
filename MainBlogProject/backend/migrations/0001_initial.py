# Generated by Django 4.1.7 on 2023-06-06 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='Category')),
                ('Date', models.DateField(max_length=100)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
    ]
