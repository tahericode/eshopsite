# Generated by Django 3.0.3 on 2021-06-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0002_auto_20210629_1653'),
        ('eshop_product', '0002_auto_20210629_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory'),
        ),
    ]