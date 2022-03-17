# Generated by Django 4.0.2 on 2022-02-22 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0019_alter_paidorder_options_alter_shipping_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='admin_remark',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='paidorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodie.paidorder'),
        ),
    ]