# Generated by Django 3.2.4 on 2021-06-13 18:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('runaways', '0002_comment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='runaway',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
