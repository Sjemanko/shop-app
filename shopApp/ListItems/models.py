from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    
    class Gender(models.TextChoices):
        MALE = "M",
        FEMALE = "FE"
    
    class ClothCategory(models.TextChoices):
        TSHIRTS = "T-Shirts",
        JACKETS = "Jackets",
        HOODIES = "Hoodies",
    
    class ProductSize(models.TextChoices):
        SMALL = "S",
        MEDIUM = "M",
        LARGE = "L",
        
        
    name = models.CharField(
        max_length=100
    )
    # discount_id = models.ForeignKey()
    # opinions = models.ForeignKey()
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=""
    )
    cloth_category = models.CharField(
        max_length=10,
        choices=ClothCategory.choices,
        default=ClothCategory.TSHIRTS
    )
    product_size = models.CharField(
        max_length=3,
        choices=ProductSize.choices,
        default=""
    )
    product_description = models.CharField(
        max_length=255,
        default=""
    )
    product_quantity = models.PositiveIntegerField(
        default=1
    )
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def validate_price(value):
        if value <= 0:
            return ValidationError("Price cannot be an negative number. Change price of product.")
        return value

    def __str__(self):
        return f'{self.id} {self.name}'
		

class Recommendation(models.Model):
    content = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.author} {self.product_id}'

