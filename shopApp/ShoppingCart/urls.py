from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.cart_view, name="cart_view"),
    path("<slug:slug>/add", views.add_product_to_cart, name="add_to_cart"),
    path("<int:id>/remove", views.remove_product_from_cart, name="remove_from_cart"),
    path("discount/", views.calculate_discount, name="calculate_discount"),
    path("submit-order/", views.submit_order, name="submit_order"),
    path("submit-order/update/", views.update_details_cart_view, name="update_details_cart_view"),
    path("submit-order/show-order-details/", views.show_order_details, name="show_order_details"),
]