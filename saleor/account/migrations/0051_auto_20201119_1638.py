# Generated by Django 3.1 on 2020-11-19 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_auto_20201119_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mobile',
            new_name='phone',
        ),
    ]