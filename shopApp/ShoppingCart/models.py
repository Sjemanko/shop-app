from django.db import models
from login.models import Profile
from ListItems.models import Product
# Create your models here.

class ShoppingCart(models.Model):
    user_profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"{self.id} {self.user_profile}"

class OrderDetail(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.id} {self.shopping_cart}"

class ProductInCart(models.Model):
    shopping_cart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True, blank=True)
    quantity = models.PositiveIntegerField(default='1')
    
    
    def __str__(self):
        return f"{self.id} {self.product} {self.quantity}"