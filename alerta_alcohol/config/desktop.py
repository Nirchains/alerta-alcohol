# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Alerta Alcohol",
			"color": "#B83A3C",
			"icon": "octicon octicon-circuit-board",
			"type": "module",
			"label": _("Alerta Alcohol"),
		},
		{
			"module_name": "Configuracion Alerta Alcohol",
			"color": "#B83A3C",
			"icon": "octicon octicon-gear",
			"type": "module",
			"label": _("Configuracion Alerta Alcohol"),
		}
	]
