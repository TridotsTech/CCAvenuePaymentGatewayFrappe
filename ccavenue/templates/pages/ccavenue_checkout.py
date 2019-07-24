# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

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


def get_context(context):
	order_id=frappe.form_dict.order_id
	if order_id:
		order_info=frappe.get_doc("Order",order_id)
		if order_info:
			if order_info.payment_status=='Pending':
				customers=frappe.db.get_all('Customers',filters={'user_id':frappe.session.user},fields=['*'])
				customer=customers[0]
				if order_info.customer==customer.name:
					context.order_info=order_info
					context.customer=customer
					gateway_settings=frappe.get_single('CCAvenue Settings')

					if gateway_settings.working_key:
						context.catalog_settings=frappe.get_single('Catalog Settings')
						context.gateway_settings=gateway_settings
					else:
						frappe.redirect_to_message(_('Some information is missing'),
					_('Looks like someone sent you to an incomplete URL. Please ask them to look into it.'))
						frappe.local.flags.redirect_location = frappe.local.response.location
						raise frappe.Redirect

				else:
					frappe.redirect_to_message(_('Some information is missing'),
					_('Looks like someone sent you to an incomplete URL. Please ask them to look into it.'))
					frappe.local.flags.redirect_location = frappe.local.response.location
					raise frappe.Redirect
			else:
				frappe.redirect_to_message(_('Some information is missing'),
					_('Looks like someone sent you to an incomplete URL. Please ask them to look into it.'))
				frappe.local.flags.redirect_location = frappe.local.response.location
				raise frappe.Redirect

		else:
			frappe.redirect_to_message(_('Some information is missing'),
			_('Looks like someone sent you to an incomplete URL. Please ask them to look into it.'))
			frappe.local.flags.redirect_location = frappe.local.response.location
			raise frappe.Redirect
	else:
		frappe.redirect_to_message(_('Some information is missing'),
			_('Looks like someone sent you to an incomplete URL. Please ask them to look into it.'))
		frappe.local.flags.redirect_location = frappe.local.response.location
		raise frappe.Redirect

 
