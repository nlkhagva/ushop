# Generated by Django 3.1 on 2020-08-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
