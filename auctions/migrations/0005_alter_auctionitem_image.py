# Generated by Django 4.2.1 on 2023-08-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctionitem_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='image',
            field=models.ImageField(blank=True, upload_to='auction_images/'),
        ),
    ]
