# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _ 

from django.db import models

# Receive modle.
class Receive(models.Model):
	receiveDate = models.DateField(verbose_name='日期')
	receiveSerialNo = models.CharField(max_length=16, verbose_name='序列号', help_text='建议使用日期加序号的方式，如201606010001')
	receiveClient = models.CharField(max_length=30, verbose_name='客户', blank=True)
	receiveMerchant = models.CharField(max_length=12, verbose_name='商品名称')
	receiveCount = models.FloatField(default=0, verbose_name='数量', blank=True)
	receivePrice = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, verbose_name='单价')
	receiveTotal = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='总价')
	receiveMaker = models.CharField(max_length=12, default='', verbose_name='经手人')
	receiveChecker = models.CharField(max_length=12, verbose_name='审核人', blank=True)
	receiveMemo = models.CharField(max_length=200, verbose_name='备注', blank=True)


	class Meta:
		verbose_name = _('收入')
		verbose_name_plural = _('收入')

class Payment(models.Model):
	payDate = models.DateField(verbose_name='日期')
	paySerialNo = models.CharField(max_length=20, verbose_name='支出凭证号', default='', blank=True)
	payClient = models.CharField(max_length=30, verbose_name='商户', blank=True)
	payMerchant = models.CharField(max_length=12, verbose_name='商品')
	payPrice = models.DecimalField(max_digits=6, decimal_places=2, default=0.0, verbose_name='单价')
	payTotal = models.DecimalField(max_digits=7, decimal_places=2, default=0.0, verbose_name='总价')
	payMaker = models.CharField(max_length=12, default='', verbose_name='经手人')
	payChecker = models.CharField(max_length=12, verbose_name='审核人', blank=True)
	payMemo = models.CharField(max_length=200, verbose_name='备注', blank=True)

	class Meta:
		verbose_name = _('支出')
		verbose_name_plural = _('支出')
