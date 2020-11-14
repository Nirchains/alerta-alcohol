# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def get_context(context):
	context.title = "Ranking de puntuaciones"

	context.parents = [{"name": _("Home"), "route": "/"},
						{"name": _("Mi cuenta"), "route": "/me"}]
	
	if not has_permissions():
		frappe.throw(_("No tiene permiso para acceder a esta página"), frappe.PermissionError)

	context.puntuaciones = frappe.get_list("Puntuaciones", fields=['name','points'], 
		filters=[
		 ['name', '!=', '[TB_ACCOUNT]']
		 ], 
		 order_by="points desc", ignore_permissions=True)
			  
def has_permissions():
	if ("Visor de Puntuaciones" in frappe.get_roles() or frappe.session.user=="Administrator"):
		return True
	else:
		return False