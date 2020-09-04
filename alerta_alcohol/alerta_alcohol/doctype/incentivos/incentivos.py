# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernandez Gomez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, cint, now, getdate
from frappe.model.document import Document

class Incentivos(Document):
	def validate(self):
		contador = cint(frappe.db.count("Incentivos", {"username": self.username, "project": self.project, "card": self.card}))
		#frappe.log_error("contador: {0}".format(contador))
		if contador > 0:
			frappe.throw("Ya ha conseguido esta carta")
