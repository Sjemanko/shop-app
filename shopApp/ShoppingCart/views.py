from django.shortcuts import render, redirect
from ListItems.models import Product
from .models import ShoppingCart, ProductInCart
from login.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def cart_view(request):
    profile = Profile.objects.get(user=request.user)
    shopping_cart = ShoppingCart.objects.get(user_profile=profile)
    items_in_cart = shopping_cart.productincart_set.all().order_by('id')
    total_product_prices = calculate_total_price_for_product(request, items_in_cart)
    total_price = calculate_total_price(request, items_in_cart)
    if request.method == 'POST' and 'quantity' in request.POST:
        new_quantity = request.POST['quantity']
        item_id = request.POST['item_id']
        changed_item = items_in_cart.get(id=item_id)
        changed_item.quantity = new_quantity
        changed_item.save()
        messages.success(request, f"Quantity of product has been changed successfully.", extra_tags="success")
        return HttpResponseRedirect(f'/cart')
    else:
        return render(request, 'ShoppingCart/cart.html', {"items_in_cart": items_in_cart, "total_cart_price": total_price, "total_product_prices": total_product_prices, "prices_data": zip(items_in_cart, total_product_prices)})

def add_product_to_cart(request, slug):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        product = Product.objects.get(slug=slug)
        if 'choosen_size' in request.POST:
            product_size = request.POST['choosen_size']
            product_in_cart = ProductInCart(shopping_cart_id=profile.shoppingcart, product=product, product_size=product_size)
            product_in_cart.save()
            messages.success(request, f"{product.name} has been added to your cart.", extra_tags='success')
            return HttpResponseRedirect(f"/products")
        else:
            messages.error(request, f"Choose size of the cloth, then add to shopping cart", extra_tags='error')
            return HttpResponseRedirect(f"/products")

def calculate_total_price(request, items_in_cart):
    total = 0
    for item in items_in_cart:
        total += item.quantity * item.product.price
    return total

def calculate_total_price_for_product(request, items_in_cart):
    prices = []
    for item in items_in_cart:
        prices.append(item.quantity * item.product.price)
    return prices