# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecPay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receive',
            name='receiveChecker',
            field=models.CharField(blank=True, max_length=12, verbose_name='\u5ba1\u6838\u4eba'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receiveClient',
            field=models.CharField(blank=True, max_length=30, verbose_name='\u5ba2\u6237'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receiveCount',
            field=models.FloatField(blank=True, default=0, verbose_name='\u6570\u91cf'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receiveMaker',
            field=models.CharField(default='', max_length=12, verbose_name='\u7ecf\u624b\u4eba'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receiveMemo',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u5907\u6ce8'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receivePrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='\u5355\u4ef7'),
        ),
        migrations.AddField(
            model_name='receive',
            name='receiveTotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='\u603b\u4ef7'),
        ),
        migrations.AlterField(
            model_name='receive',
            name='receiveSerialNo',
            field=models.CharField(help_text='\u5efa\u8bae\u4f7f\u7528\u65e5\u671f\u52a0\u5e8f\u53f7\u7684\u65b9\u5f0f\uff0c\u5982201606010001', max_length=16, verbose_name='\u5e8f\u5217\u53f7'),
        ),
    ]
