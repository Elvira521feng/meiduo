# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 02:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180923_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sku',
            options={'ordering': ['-create_time'], 'verbose_name': '商品SKU', 'verbose_name_plural': '商品SKU'},
        ),
    ]
