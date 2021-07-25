"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from eshop.settings import DEBUG
from django.contrib import admin
from django.urls import path, include
from .import settings
from django.conf.urls.static import static
from .views import footer, home_page ,header,about_page

urlpatterns = [
    path('',home_page),
    path('header' ,header ,name='header'),
    path('footer',footer, name='footer'),
    path('admin/', admin.site.urls),
    path('about-us',about_page),
    path('',include('eshop_account.urls')),
    path('',include('eshop_product.urls')),
    path('',include('eshop_contact.urls')),
    path('',include('eshop_order.urls'))
]

if settings.DEBUG:
    # add root static files
    urlpatternsl = urlpatterns + static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    # add root media files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
