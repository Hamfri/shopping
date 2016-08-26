# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160504_1219'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('shipping_name', models.CharField(max_length=50)),
                ('shipping_address_1', models.CharField(max_length=50)),
                ('shipping_address_2', models.CharField(max_length=50, blank=True)),
                ('shipping_city', models.CharField(max_length=50)),
                ('shipping_state', models.CharField(max_length=50)),
                ('shipping_country', models.CharField(max_length=50)),
                ('shipping_zip', models.CharField(max_length=10)),
                ('billing_name', models.CharField(max_length=50)),
                ('billing_address_1', models.CharField(max_length=50)),
                ('billing_address_2', models.CharField(max_length=50, blank=True)),
                ('billing_city', models.CharField(max_length=50)),
                ('billing_state', models.CharField(max_length=2)),
                ('billing_country', models.CharField(max_length=50)),
                ('billing_zip', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Submitted'), (2, b'Processed'), (3, b'Shipped'), (4, b'Cancelled')])),
                ('ip_address', models.GenericIPAddressField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('order', models.ForeignKey(to='checkout.Order')),
                ('product', models.ForeignKey(to='catalog.Product')),
            ],
        ),
    ]
