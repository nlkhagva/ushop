# Generated by Django 3.1 on 2020-11-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0047_auto_20200810_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
