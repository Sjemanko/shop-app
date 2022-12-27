from django.contrib import admin
from .models import Product, Recommendation


# Register your models here.
 
class RecommendationAdmin(admin.ModelAdmin):
  	list_display = ['author', 'content', 'product_id']


class RecommendationInLine(admin.StackedInline):
	model = Recommendation
	extra = 0

class ProductAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'gender', 'cloth_category', 'product_size', 'product_description', 'product_quantity', 'price', 'image']
	inlines = [RecommendationInLine]
	extra = 0


admin.site.register(Product, ProductAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
