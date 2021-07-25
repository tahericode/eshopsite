from eshop_product.models import Product
from django.shortcuts import render,redirect
from eshop_sliders.models import Slider
from eshop_settings.models import SiteSetting
import itertools
# header code behind        .................................................................

def header(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Header.html',context)

# footer code behind        .................................................................
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting' : site_setting
   
    }
    return render(request, 'shared/Footer.html',context)


# my grouper               ...................................................................
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))
 

# home page                ...................................................................
def home_page(request):
    slider = Slider.objects.all()
    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    context = {
        'data':'new data',
        'sliders':slider,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products':my_grouper(4, latest_products)
    }
    return render(request,"home_page.html", context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }
    return render(request, 'about_page.html', context )
