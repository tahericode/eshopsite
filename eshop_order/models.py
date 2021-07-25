from re import U
import re
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from eshop_product.models import Product
# Create your models here.

class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده', default= False)
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید کاربران'
    def __str__(self):
        return str(self.owner)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name='سبد خرید')
    product = models.ForeignKey(Product,on_delete=CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price



    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'
    def __str__(self):
        return self.product.title