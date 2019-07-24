# -*- coding: utf-8 -*-
# Copyright (c) 2018, info@valiantsystems.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class CCAvenueSettings(Document):
	def on_update(self):
		payment_method=frappe.db.get_all('Payment Method',filters={"payment_method":"CCAvenue"},order_by='display_order',fields=['*'])
		if not payment_method:
			doc=frappe.new_doc("Payment Method")
			doc.payment_method="CCAvenue"
			doc.display_order=1
			doc.enable=1
			doc.payment_type="Online Payment"
			doc.additional_charge=0
			doc.save()

