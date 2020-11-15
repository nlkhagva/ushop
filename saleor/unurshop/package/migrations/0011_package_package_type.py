# Generated by Django 3.1 on 2020-11-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0010_auto_20200921_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_type',
            field=models.CharField(choices=[('order', 'Захиалга'), ('self', 'Өөрөө авах'), ('cargo', 'Илгээмж')], default='order', max_length=32),
        ),
    ]
