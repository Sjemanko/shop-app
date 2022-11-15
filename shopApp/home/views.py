from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def home_page(request):
    return render(request, 'home.html')


def product_page(request, gender, category):
    return render(request, 'product_page.html', {'gender': gender, 'category': category})
