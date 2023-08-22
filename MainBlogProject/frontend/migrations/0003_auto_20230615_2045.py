# Generated by Django 3.2.10 on 2023-06-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_usercategorydb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblogdb',
            name='Author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='Blog_Image',
            field=models.ImageField(upload_to='Blogs'),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='Blog_Title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='Category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='City',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='Content',
            field=models.CharField(max_length=10000000),
        ),
        migrations.AlterField(
            model_name='userblogdb',
            name='Date',
            field=models.DateField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usercategorydb',
            name='Category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usercategorydb',
            name='Description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='usercategorydb',
            name='Image',
            field=models.ImageField(upload_to='Category'),
        ),
    ]