# Generated by Django 4.0.3 on 2022-04-04 13:05

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0017_remove_car_commission_remove_car_commission_currency_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyer',
            old_name='commision_currency',
            new_name='commission_currency',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='commision',
        ),
        migrations.AddField(
            model_name='buyer',
            name='commission',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=10),
        ),
    ]
