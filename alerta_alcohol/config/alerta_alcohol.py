from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Alerta Alcohol"),
			"icon": "fa fa-exclamation",
			"items": [
				{
					"type": "doctype",
					"name": "Incentivos",
					"description": _("Incentivos"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Puntuaciones",
					"description": _("Puntuaciones"),
					"onboard": 1,
				}
			]
		}
	]