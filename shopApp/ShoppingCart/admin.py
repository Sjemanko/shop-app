from django.contrib import admin
from .models import OrderDetail, ShoppingCart, ProductInCart
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
  	list_display = ['id', 'shopping_cart']


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_profile']
    
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['shopping_cart_id', 'product', 'quantity']


admin.site.register(OrderDetail, OrderAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)