# Generated by Django 4.0.2 on 2022-03-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0006_remove_shipping_quantity_remove_shipping_spice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='paidorder',
        ),
        migrations.DeleteModel(
            name='PaidOrder',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]
