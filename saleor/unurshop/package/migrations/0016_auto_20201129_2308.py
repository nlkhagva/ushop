# Generated by Django 3.1 on 2020-11-29 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0101_fulfillmentline_package_line'),
        ('package', '0015_auto_20201129_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageline',
            name='fulfillmentline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fulfillmentlines', to='order.fulfillmentline'),
        ),
    ]
