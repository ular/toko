# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 09:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160218_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_product_categories', to='products.Product'),
        ),
    ]
