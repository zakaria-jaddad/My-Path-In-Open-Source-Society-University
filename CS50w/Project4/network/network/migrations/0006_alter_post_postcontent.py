# Generated by Django 4.1.7 on 2023-07-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_post_postimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postContent',
            field=models.TextField(max_length=150),
        ),
    ]