# Generated by Django 3.1.7 on 2021-12-18 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileLearning', '0029_auto_20211214_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='lection',
            name='direction',
            field=models.CharField(default='ALL', max_length=50, verbose_name='Направление подготовки'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 12, 18, 15, 42, 0, 835433), verbose_name='Дата рождения'),
        ),
    ]
