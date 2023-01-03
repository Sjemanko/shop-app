from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_all_products, name="products_list"),
    path("<str:slug>/", views.product_details_page, name="product_details")
]