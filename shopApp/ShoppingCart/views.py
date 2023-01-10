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
    items_in_cart = shopping_cart.productincart_set.all()
    print(items_in_cart)
    return render(request, 'ShoppingCart/cart.html', {"items_in_cart": items_in_cart})

def add_product_to_cart(request, slug):
    profile = Profile.objects.get(user=request.user)
    print(request.path)
    if request.method == "POST":
        product = Product.objects.get(slug=slug)
        if 'choosen_size' in request.POST:
            product_size = request.POST['choosen_size']
            product_in_cart = ProductInCart(shopping_cart_id=profile.shoppingcart, product=product)
            product_in_cart.save()
            messages.success(request, f"{product.name} has been added to your cart.", extra_tags='success')
            return HttpResponseRedirect(f"/products")
        else:
            messages.error(request, f"Choose size of the cloth, then add to shopping cart", extra_tags='error')
            return HttpResponseRedirect(f"/products")