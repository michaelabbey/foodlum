# Generated by Django 4.0.2 on 2022-02-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='how_spicey',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
