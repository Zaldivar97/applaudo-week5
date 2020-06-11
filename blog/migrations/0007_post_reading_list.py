# Generated by Django 3.0.7 on 2020-06-11 06:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20200610_0623'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reading_list',
            field=models.ManyToManyField(related_name='reading_list', to=settings.AUTH_USER_MODEL),
        ),
    ]
