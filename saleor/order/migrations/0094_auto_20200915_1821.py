# Generated by Django 3.1 on 2020-09-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0093_fulfillmentline_ushop_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillmentline',
            name='changed_date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='fulfillmentline',
            name='soon_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
