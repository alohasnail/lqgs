# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiveDate', models.DateField(verbose_name='\u65e5\u671f')),
                ('receiveSerialNo', models.CharField(max_length=16, verbose_name='\u5e8f\u5217\u53f7')),
                ('receiveMerchant', models.CharField(max_length=12, verbose_name='\u5546\u54c1\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u6536\u5165',
                'verbose_name_plural': '\u6536\u5165',
            },
        ),
    ]
