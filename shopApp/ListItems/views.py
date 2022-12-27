from django.shortcuts import render
from .models import Product

# Create your views here.

def product_page(request, gender, category):
    return render(request, 'ListItems/product_page.html', {'gender': gender, 'category': category})

def show_all_products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'ListItems/products.html', {'item_list': products })