# Generated by Django 4.0.2 on 2022-02-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0003_variety_slug_alter_variety_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
