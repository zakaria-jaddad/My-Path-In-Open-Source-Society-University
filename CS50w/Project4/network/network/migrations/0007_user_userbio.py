# Generated by Django 4.1.7 on 2023-07-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_post_postcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userBio',
            field=models.TextField(max_length=300, null=True),
        ),
    ]