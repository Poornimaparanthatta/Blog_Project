# Generated by Django 3.2.10 on 2023-06-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_rename_category_name_blogdb_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdb',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
