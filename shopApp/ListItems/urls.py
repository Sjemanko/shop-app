from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.show_all_products, name="products_list"),
    path("<str:gender>/<str:category>/", views.product_page, name='gender_category'),
]

