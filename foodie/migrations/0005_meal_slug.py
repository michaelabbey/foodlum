# Generated by Django 4.0.2 on 2022-02-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0004_alter_variety_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(default='a', unique=True),
        ),
    ]
