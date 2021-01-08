# Generated by Django 3.1 on 2020-09-14 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0091_fulfillment_uk_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='fulfillment',
            name='firstname',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='fulfillment',
            name='lastname',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AddField(
            model_name='fulfillment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ordersfulfillment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fulfillment',
            name='ushop_status',
            field=models.CharField(choices=[('new', 'New'), ('atuk', 'Англид ирсэн'), ('shipping', 'Тээвэрт орсон'), ('atmgl', 'Монголд ирсэн'), ('received', 'Хэрэглэгч хүлээж авсан')], default='new', max_length=32),
        ),
    ]
