from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'gender', 'cloth_category', 'product_size', 'product_description', 'quantity', 'price', 'image']
 
 
admin.site.register(Product, ProductAdmin)
 
