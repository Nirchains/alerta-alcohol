from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Configuracion Alerta Alcohol"),
			"icon": "fa fa-group",
			"items": [
				{
					"type": "doctype",
					"name": "Proyecto",
					"description": _("Proyectos"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Carta",
					"description": _("Carta"),
					"onboard": 1,
				}
			]
		}
	]