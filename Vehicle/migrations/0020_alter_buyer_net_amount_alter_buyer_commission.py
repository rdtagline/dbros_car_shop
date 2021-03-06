# Generated by Django 4.0.3 on 2022-04-05 04:02

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0019_alter_buyer_net_amount_alter_buyer_commission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='Net_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='commission',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='USD', max_digits=10),
        ),
    ]
