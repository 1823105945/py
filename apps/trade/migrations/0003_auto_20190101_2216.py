# Generated by Django 2.1.4 on 2019-01-01 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20181231_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfor',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 1, 22, 16, 9, 945492), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 1, 22, 16, 9, 945492), verbose_name='添加时间'),
        ),
    ]
