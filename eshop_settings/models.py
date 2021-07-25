from django.db import models
import os
# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.title}{ext}"
    return f"logo-image/{final_name}"

class SiteSetting(models.Model):
    title = models.CharField(max_length=150 , verbose_name='عنوان سایت')
    address = models.CharField(max_length=400 , verbose_name='نشانی')
    phone = models.CharField(max_length=150 , verbose_name='تلفن محل کار')
    mobile = models.CharField(max_length=150 , verbose_name='موبایل')
    fax = models.CharField(max_length=150 , verbose_name='فکس')
    email = models.CharField(max_length=150 , verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما',null=True, blank=True)
    logo_image = models.ImageField(upload_to=upload_image_path, verbose_name='تصویر لوگو', null = True, blank = True)

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت تنظیمات'

    def __str__(self):
        return self.title