from django.db import models
from django.db.models.fields import CharField
import os
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

def upload_image_path(instanse, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instanse.id}-{instanse.title}{ext}"
    return f"sliders/{final_name}"



class Slider(models.Model):
    title = models.CharField(max_length=150,verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name= 'ادرس')
    descriptions = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='تصویر')


    class Meta:
        verbose_name = 'اسلاید'
        verbose_name_plural = 'اسلایدها'

    def __str__(self):
        return self.title