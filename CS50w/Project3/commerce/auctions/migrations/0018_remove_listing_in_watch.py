# Generated by Django 4.1.7 on 2023-06-04 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_userbid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='in_watch',
        ),
    ]