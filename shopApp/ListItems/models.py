from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify

# Create your models here.
class ModifiedArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            **kwargs
        }
        return super(ArrayField, self).formfield(**defaults)


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
        max_length=100,
        unique=True
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
    product_size = ModifiedArrayField(models.CharField(
            max_length=50,
            choices=ProductSize.choices,
            default=ProductSize.SMALL
        ),
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
    slug = models.SlugField(blank=True, null=True)
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

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} {self.name}'
		

class Recommendation(models.Model):
    content = models.TextField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id} {self.author} {self.product_id}'

