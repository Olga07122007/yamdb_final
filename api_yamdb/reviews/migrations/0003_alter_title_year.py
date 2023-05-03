# Generated by Django 3.2 on 2023-02-06 19:40

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[api.validators.validate_year], verbose_name='Дата выхода'),
        ),
    ]
