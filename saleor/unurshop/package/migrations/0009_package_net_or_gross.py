# Generated by Django 3.1 on 2020-09-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0008_auto_20200918_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='net_or_gross',
            field=models.CharField(choices=[('net', 'Цэвэр жин'), ('gross', 'Оврийн жин')], default='net', max_length=16),
        ),
    ]
