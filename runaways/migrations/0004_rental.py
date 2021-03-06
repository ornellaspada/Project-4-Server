# Generated by Django 3.2.4 on 2021-06-14 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runaways', '0003_runaway_favorited_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_rented', models.DateField(max_length=250)),
                ('date_returned', models.DateField(max_length=250, null=True)),
                ('rented', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL)),
                ('runaway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='runaways.runaway')),
            ],
        ),
    ]
