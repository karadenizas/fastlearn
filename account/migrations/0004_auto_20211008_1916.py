# Generated by Django 3.2.8 on 2021-10-08 19:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_mycourse_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycourse',
            name='user',
        ),
        migrations.AddField(
            model_name='mycourse',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
