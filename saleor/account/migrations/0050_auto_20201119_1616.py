# Generated by Django 3.1 on 2020-11-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0049_auto_20201119_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
