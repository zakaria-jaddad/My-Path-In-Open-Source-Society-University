# Generated by Django 4.1.7 on 2023-06-06 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_rename_categorys_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbid',
            name='user_new_bid',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
