# Generated by Django 4.1.7 on 2023-06-06 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_alter_categorys_listing_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorys',
            new_name='Categories',
        ),
    ]
