# Generated by Django 4.2.4 on 2023-08-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimtblog', '0003_popular_blog_image_alter_regular_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='regular_blog',
            name='image',
            field=models.ImageField(default='', upload_to='image'),
        ),
    ]
