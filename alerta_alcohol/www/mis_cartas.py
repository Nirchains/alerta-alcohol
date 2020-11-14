# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernández Gómez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def get_context(context):
	context.title = "Mis cartas"

	context.parents = [{"name": _("Home"), "route": "/"},
						{"name": _("Mi cuenta"), "route": "/me"}]
	
	if not has_permissions():
		frappe.throw(_("No tiene permiso para acceder a esta página"), frappe.PermissionError)

	context.usuario = frappe.db.get_value("User",frappe.session.user, fieldname="username")
	#context.usuario = frappe.session.user

	context.cartas = frappe.db.sql(""" select tc.image, tc.card_name
		from `tabIncentivos` ti inner join `tabCarta` tc on ti.card = tc.name 
		where ti.username = %s
		order by tc.name asc""", (context.usuario), as_dict=True)


def has_permissions():
	if ("Visor de Puntuaciones" in frappe.get_roles() or frappe.session.user=="Administrator"):
		return True
	else:
		return False