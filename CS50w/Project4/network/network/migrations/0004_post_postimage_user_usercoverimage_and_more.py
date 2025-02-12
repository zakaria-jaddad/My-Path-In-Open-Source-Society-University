# Generated by Django 4.1.7 on 2023-07-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post_timepublish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postImage',
            field=models.FileField(null=True, upload_to='posts/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='userCoverImage',
            field=models.ImageField(null=True, upload_to='covers_images/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='user',
            name='userProfileImage',
            field=models.ImageField(null=True, upload_to='profile_images/', verbose_name=''),
        ),
    ]
