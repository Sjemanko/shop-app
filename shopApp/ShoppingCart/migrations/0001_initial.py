# Generated by Django 4.2 on 2023-04-07 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('ListItems', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_name', models.CharField(max_length=255)),
                ('discount_percent', models.FloatField(max_length=5)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.profile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ShoppingCart.shoppingcart')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default='1')),
                ('product_size', models.CharField(default='', max_length=1)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ListItems.product')),
                ('shopping_cart_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ShoppingCart.shoppingcart')),
            ],
            options={
                'unique_together': {('shopping_cart_id', 'product', 'product_size')},
            },
        ),
    ]
