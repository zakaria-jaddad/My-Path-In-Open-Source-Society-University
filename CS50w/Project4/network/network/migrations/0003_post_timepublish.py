# Generated by Django 4.1.7 on 2023-07-14 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_post_likedpost_following_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timePublish',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
