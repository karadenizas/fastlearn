# Generated by Django 3.2.8 on 2021-10-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flearn', '0003_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]