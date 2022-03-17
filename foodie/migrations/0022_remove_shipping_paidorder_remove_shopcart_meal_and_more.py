# Generated by Django 4.0.2 on 2022-02-24 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0021_meal_max_order_meal_min_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='paidorder',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='shopcart',
            name='user',
        ),
        migrations.DeleteModel(
            name='PaidOrder',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
        migrations.DeleteModel(
            name='Shopcart',
        ),
    ]
