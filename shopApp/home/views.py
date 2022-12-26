from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Product

# Create your views here.

def home_page(request):
    item_list = Product.objects.all()
    print(item_list.last().image)
    return render(request, 'home.html', {'item_list': item_list} )


def product_page(request, gender, category):
    return render(request, 'product_page.html', {'gender': gender, 'category': category})
