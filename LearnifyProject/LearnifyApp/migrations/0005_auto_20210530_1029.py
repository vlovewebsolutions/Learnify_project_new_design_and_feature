# Generated by Django 3.1.7 on 2021-05-30 04:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnifyApp', '0004_auto_20210530_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesstructure',
            name='year_session',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(regex='\\d{4}-\\d{2}')], verbose_name='Session should be like 2020-21'),
        ),
    ]
