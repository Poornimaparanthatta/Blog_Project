# Generated by Django 3.2.10 on 2023-06-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_auto_20230615_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdb',
            name='Author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='Blog_Image',
            field=models.ImageField(blank=True, null=True, upload_to='Blogs'),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='Blog_Title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='Content',
            field=models.CharField(blank=True, max_length=10000000, null=True),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='Date',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='categorydb',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Category'),
        ),
    ]
