# Generated by Django 3.0.3 on 2021-06-14 07:11

from django.db import migrations, models
import eshop_product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('descriptions', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_product.models.upload_image_path)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]