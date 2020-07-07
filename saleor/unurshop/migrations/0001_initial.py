# Generated by Django 3.0.6 on 2020-06-27 06:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import draftjs_sanitizer
import saleor.core.db.fields
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('seo_title', models.CharField(blank=True, max_length=70, null=True, validators=[django.core.validators.MaxLengthValidator(70)])),
                ('seo_description', models.CharField(blank=True, max_length=300, null=True, validators=[django.core.validators.MaxLengthValidator(300)])),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('logo_image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='unurshop-shop')),
                ('logo_image_alt', models.CharField(blank=True, max_length=128)),
                ('description', models.TextField(blank=True)),
                ('description_json', saleor.core.db.fields.SanitizedJSONField(blank=True, default=dict, sanitizer=draftjs_sanitizer.clean_draft_js)),
                ('rank', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_main', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_uk_shipping', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_product_quality', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_product_price', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_shuurhai', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rating_product_rank', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('shipment_fee', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('shipping_fee_yaraltai', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('shipping_fee_free', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('shipping_deliver_yaraltai', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_deliver_standart', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_deliver_free', models.CharField(blank=True, max_length=50, null=True)),
                ('has_shipping_tax', models.BooleanField(default=False)),
                ('shipping_per_product', models.BooleanField(default=False)),
                ('open_graph', models.BooleanField(default=False)),
                ('autofill', models.BooleanField(default=True)),
                ('xero_id', models.CharField(blank=True, default=0, max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('listSelection', models.TextField(blank=True)),
                ('productSelection', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crawler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('url', models.URLField(unique=True)),
                ('completed', models.BooleanField(default=False)),
                ('crawled_at', models.DateTimeField(auto_now=True, null=True)),
                ('product_count', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('json_data', saleor.core.db.fields.SanitizedJSONField(blank=True, default=dict, sanitizer=draftjs_sanitizer.clean_draft_js)),
                ('json_data_backup', saleor.core.db.fields.SanitizedJSONField(blank=True, default=dict, sanitizer=draftjs_sanitizer.clean_draft_js)),
                ('listSelection', models.TextField(blank=True)),
                ('productSelection', models.TextField(blank=True)),
                ('shop', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='crawlers', to='unurshop.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
