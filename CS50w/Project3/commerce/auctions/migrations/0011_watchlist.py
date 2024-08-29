# Generated by Django 4.1.7 on 2023-06-03 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_listing_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listing_id', to='auctions.listing')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings_of_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]