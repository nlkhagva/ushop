# Generated by Django 3.1 on 2020-08-24 05:54

from django.db import migrations, models
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0028_merge_20200818_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutline',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutline',
            name='private_metadata',
            field=models.JSONField(blank=True, default=dict, encoder=saleor.core.utils.json_serializer.CustomJsonEncoder, null=True),
        ),
    ]
