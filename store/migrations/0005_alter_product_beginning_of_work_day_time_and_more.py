# Generated by Django 4.2.2 on 2023-09-05 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_beginning_of_work_day_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='beginning_of_work_day_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='end_of_work_day_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
