# Generated by Django 4.1.7 on 2023-06-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.TextField(blank=True),
        ),
    ]
