# Generated by Django 4.2.11 on 2024-04-27 13:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
