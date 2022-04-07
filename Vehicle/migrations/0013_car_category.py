# Generated by Django 4.0.3 on 2022-03-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0012_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('New', 'New'), ('Used', 'Used'), ('Select', 'Select')], default='Select', max_length=50),
        ),
    ]