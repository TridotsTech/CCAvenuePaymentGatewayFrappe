#!/usr/bin/python
from __future__ import unicode_literals
# import frappe
# from _future_ import unicode_literals
import frappe
from frappe import async
import frappe.utils
import json
import calendar
import razorpay
from frappe import _
from frappe.utils import getdate,nowdate
from datetime import date

def get_context(context,**kwargs):
	print('-----Payment Response------')
	kwargs=frappe._dict(kwargs)
	print(kwargs)
def ccavenue_payment_response(**kwargs):
	kwargs=frappe._dict(kwargs)
	print(kwargs)