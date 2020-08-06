# Generated by Django 3.0.6 on 2020-06-25 11:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0083_merge_20200421_0529'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
        migrations.AddField(
            model_name='orderline',
            name='private_metadata',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
    ]
