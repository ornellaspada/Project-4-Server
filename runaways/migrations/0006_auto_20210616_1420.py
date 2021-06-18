# Generated by Django 3.2.4 on 2021-06-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('runaways', '0005_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='runaway',
            name='price',
        ),
        migrations.AddField(
            model_name='runaway',
            name='rent_price',
            field=models.CharField(default='rent_price: $20 per day', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='runaway',
            name='sale_price',
            field=models.CharField(default='sale_price: 3000', max_length=200),
            preserve_default=False,
        ),
    ]
