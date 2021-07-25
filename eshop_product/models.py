from eshop_products_category.models import ProductCategory
from django.db.models import Q, lookups 
from django.db import models
from django.db.models.base import Model
import os

from django.db.models.manager import Manager
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.id}-{instanse.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.id}-{instanse.title}{ext}"
    return f"products/gallery/{final_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(category__name__iexact=category_name, active = True)
    
    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1 :
            return qs.first()
        else:
            return None
    # in def ro baraye search minevisim va dar view az in optione jadide objects estefade mikonim
    def search(self,query):
        lookup =(
            Q(title__icontains=query) | 
            Q(descriptions__icontains=query) |
            Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter( lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    descriptions = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    category = models.ManyToManyField(ProductCategory,blank=True)
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return f"/product/{self.id}/{self.title.replace(' ','-')}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name="عنوان")
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='تصویر')
    Product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="محصول")


    class Meta:
        verbose_name = 'گالری محصول'
        verbose_name_plural = 'گالری محصولات'

    def __str__(self):
        return self.title 