# Generated by Django 3.1 on 2020-08-28 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_package_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageline',
            old_name='order_line',
            new_name='orderline',
        ),
    ]