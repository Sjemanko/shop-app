from django.shortcuts import render, redirect
from ListItems.models import Product
from .models import ShoppingCart, ProductInCart, DiscountCode, OrderDetail
from login.models import Profile
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from login.forms import NewUserForm, UserDetailsForm
from login.views import save_data_details
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

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
        if request.GET.get('used_code', ''):
            total_price = request.GET.get('total')
        return render(request, 'ShoppingCart/cart.html', {"items_in_cart": items_in_cart, "total_cart_price": total_price, "total_product_prices": total_product_prices, "prices_data": zip(items_in_cart, total_product_prices)})
           
        
def add_product_to_cart(request, slug):
    profile = Profile.objects.get(user=request.user)
    if_product_in_cart = False
    if request.method == "POST":
        product = Product.objects.get(slug=slug)
        if 'choosen_size' in request.POST:
            product_size = request.POST['choosen_size']
            if_product_in_cart = check_if_product_in_cart(request, slug, product_size, profile)
            if if_product_in_cart:
                messages.error(request, f"{product.name} is already in shopping cart", extra_tags='error')
                return HttpResponseRedirect(f"/products")
            else:
                product_in_cart = ProductInCart(shopping_cart_id=profile.shoppingcart, product=product, product_size=product_size)
                product_in_cart.save()
                messages.success(request, f"{product.name} has been added to your cart.", extra_tags='success')
                return HttpResponseRedirect(f"/products")           
        else:
            messages.error(request, f"Choose size of the cloth, then add to shopping cart", extra_tags='error')
            return HttpResponseRedirect(f"/products")

def calculate_discount(request):
    used_code = False
    if request.method == "POST" and request.POST['discount_code'] != "":
        profile = Profile.objects.get(user=request.user)
        shopping_cart = ShoppingCart.objects.get(user_profile=profile)
        items_in_cart = shopping_cart.productincart_set.all().order_by('id')
        code = request.POST['discount_code']
        discount = DiscountCode.objects.get(code_name=code)
        if code:
            used_code = True
        discount_value = round((float(calculate_total_price(request, items_in_cart)) * float(discount.discount_percent)) / 100, 2)
        total_value = round(float(calculate_total_price(request, items_in_cart)) - float(discount_value), 2)
        messages.success(request, f"Your discount code has been applied.", extra_tags="success")
        return HttpResponseRedirect(f"/cart?used_code=True&total={total_value}")
    else:
        messages.error(request, f"Your discount code is not valid.", extra_tags="error")
        return HttpResponseRedirect(f'/cart')

def submit_order(request):
    used_code = False
    profile = Profile.objects.get(user=request.user)
    shopping_cart = ShoppingCart.objects.get(user_profile=profile)
    items_in_cart = shopping_cart.productincart_set.all().order_by('id')
    total_product_prices = calculate_total_price_for_product(request, items_in_cart)
    total_price = calculate_total_price(request, items_in_cart)
    submitted = False
    if request.method == "POST":
        save_data_details(request, f'/cart/submit-order')
    else:
        form = UserDetailsForm
        if request.GET.get('used_code', ''):
            total_price = request.GET.get('total')
        if Profile.objects.filter(user=request.user.id).exists():
            profile_details = Profile.objects.get(user=request.user.id)
            submitted = True
            form = UserDetailsForm(request.POST or None, instance=profile_details)
            return render(request, 'ShoppingCart/confirm_order.html', {"form": form, "submitted": submitted, "total_price": total_price, "profile_details": profile_details,"total_product_prices": total_product_prices, 'items_in_cart': items_in_cart, "prices_data": zip(items_in_cart, total_product_prices)})
    return render(request, 'ShoppingCart/confirm_order.html', {"form": form, 'items_in_cart': items_in_cart, "total_price": total_price, "total_product_prices": total_product_prices, "prices_data": zip(items_in_cart, total_product_prices)})

def remove_product_from_cart(request, id):
    product = ProductInCart.objects.get(id=id)
    product.delete()
    return  HttpResponseRedirect(f"/cart")

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

def check_if_product_in_cart(request, slug, product_size, profile):
    return ProductInCart.objects.filter(product__slug=slug, product_size=product_size, shopping_cart_id__user_profile=profile)

def update_details_cart_view(request):
    profile_details = Profile.objects.get(user=request.user.id)
    form = UserDetailsForm(request.POST or None, instance=profile_details)
    if form.is_valid():
        form.save()
        messages.success(request, f"Your data has been updated")
        return HttpResponseRedirect(f'/cart/submit-order')
    else:
        messages.error(request, f"Form is not valid. Check form and correct fields.")
    return render(request, 'ShoppingCart/confirm_order.html', {"form": form, "submitted": submitted})


def show_order_details(request):
    shopping_cart = ShoppingCart.objects.get(user_profile__user=request.user)
    profile = Profile.objects.get(user=request.user)
    shopping_cart_items = ShoppingCart.objects.get(user_profile=profile).productincart_set.all().order_by('id')
    total_product_prices = calculate_total_price_for_product(request, shopping_cart_items)
    
    if request.method == "POST" and 'shipping-method' in request.POST:
        shipping_method = request.POST['shipping-method']
        total_price = request.POST['total_price']
        
        msg_plain = render_to_string('ShoppingCart/email_confirmation_text.txt', {"shopping_cart": shopping_cart, "profile": profile, "shopping_cart_items": shopping_cart_items, "shipping_method": shipping_method, "total_price": total_price, "total_product_prices": total_product_prices, "prices_data": zip(shopping_cart_items, total_product_prices)})
        msg_html = render_to_string('ShoppingCart/email_confirmation_text.html', {"shopping_cart": shopping_cart, "profile": profile, "shopping_cart_items": shopping_cart_items, "shipping_method": shipping_method, "total_price": total_price, "total_product_prices": total_product_prices, "prices_data": zip(shopping_cart_items, total_product_prices)})

        # Dane email wpisywane na sztywno 
        send_mail(
            'Ordered Items',
            msg_plain,
            'cypresstests@spoko.pl',
            ['piyexik119@fom8.com'],
            html_message=msg_html,
        )
        messages.success(request, f"The purchase has been confirmed. Check your mailbox.", extra_tags="success")
    else:
        messages.error(request, f"Complete the means of transportation.", extra_tags="error")
        return HttpResponseRedirect(f'/cart/submit-order')
    return render(request, 'sender/email_confirmation.html', {"shopping_cart": shopping_cart, "profile": profile, "shopping_cart_items": shopping_cart_items, "shipping_method": shipping_method, "total_price": total_price})


def send_email_notification(request):
    
    return render(request, 'sender/email_confirmation.html')
