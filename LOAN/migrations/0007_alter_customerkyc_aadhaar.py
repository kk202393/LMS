# Generated by Django 4.0.2 on 2022-07-09 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOAN', '0006_delete_allimage_customerkyc_aadharimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerkyc',
            name='Aadhaar',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(14)]),
        ),
    ]
