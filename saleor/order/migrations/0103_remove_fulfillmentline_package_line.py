# Generated by Django 3.1 on 2020-12-11 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0102_auto_20201201_2227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fulfillmentline',
            name='package_line',
        ),
    ]
