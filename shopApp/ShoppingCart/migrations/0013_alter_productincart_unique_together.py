# Generated by Django 4.1.5 on 2023-01-19 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingCart', '0012_remove_productincart_shopping_cart_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productincart',
            unique_together=set(),
        ),
    ]
