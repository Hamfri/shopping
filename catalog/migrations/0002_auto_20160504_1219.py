# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=datetime.datetime(2016, 5, 4, 12, 19, 27, 352909, tzinfo=utc), upload_to=b'images/products/main'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image_caption',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=b'images/products/thumbnails'),
            preserve_default=False,
        ),
    ]
