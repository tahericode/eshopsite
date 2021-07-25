from django.contrib import admin
from django.db import models
from .models import ProductCategory
# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=['__str__', 'title']

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)