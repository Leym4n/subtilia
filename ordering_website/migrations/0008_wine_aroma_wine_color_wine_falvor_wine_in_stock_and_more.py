# Generated by Django 4.0.2 on 2022-11-10 21:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering_website', '0007_delete_wineimage_wine_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='aroma',
            field=models.CharField(default='no aroma', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='color',
            field=models.CharField(default='no color', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='falvor',
            field=models.CharField(default='no flavor', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='in_stock',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='producer',
            field=models.CharField(default='no producer', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wine',
            name='strain',
            field=models.CharField(default='no strain', max_length=100),
            preserve_default=False,
        ),
    ]
