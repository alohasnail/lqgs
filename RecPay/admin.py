# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import Receive, Payment


class ReceiveAdmin(admin.ModelAdmin):
    fields = ['receiveDate', 'receiveSerialNo', 'receiveClient', 'receiveMerchant', 'receiveCount',
              'receivePrice', 'receiveTotal', 'receiveMaker', 'receiveChecker', 'receiveMemo']
    list_display = ('receiveDate', 'receiveSerialNo', 'receiveClient',
                    'receiveMerchant', 'receiveTotal', 'receiveMaker', 'receiveChecker')

class PaymentAdmin(admin.ModelAdmin):
	fields = ['payDate', 'paySerialNo', 'payClient', 'payMerchant', 
				'payPrice', 'payTotal', 'payMaker', 'payChecker', 'payMemo']
	list_display = ('payDate', 'paySerialNo', 'payClient', 'payMerchant','payTotal', 'payMaker')

admin.site.register(Receive, ReceiveAdmin)
admin.site.register(Payment, PaymentAdmin)
