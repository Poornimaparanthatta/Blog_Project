# Generated by Django 3.2.10 on 2023-06-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBlogDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Blog_Title', models.CharField(blank=True, max_length=500, null=True)),
                ('Date', models.DateField(blank=True, max_length=100, null=True)),
                ('Author', models.CharField(blank=True, max_length=100, null=True)),
                ('Blog_Image', models.ImageField(blank=True, null=True, upload_to='Blogs')),
                ('City', models.CharField(blank=True, max_length=100, null=True)),
                ('Content', models.CharField(blank=True, max_length=10000000, null=True)),
            ],
        ),
    ]
