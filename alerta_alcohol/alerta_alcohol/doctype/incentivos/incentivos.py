# -*- coding: utf-8 -*-
# Copyright (c) 2020, Pedro Antonio Fernandez Gomez and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import nowdate, cstr, flt, cint, now, getdate
from frappe.model.document import Document

class Incentivos(Document):
	def validate(self):
		if frappe.db.exists("Incentivos", {"username": self.username, "project": self.project, "card": self.card}):
			frappe.throw("Ya ha conseguido esta card")

@frappe.whitelist(allow_guest = True)
def alerta_puntuacion(username, fullname, email, project, card):
	if not frappe.db.exists('User', email):
		user = frappe.new_doc('User')
		user.email = email
		user.first_name = fullname
		user.username = username
		user.save(ignore_permissions=True)
		asignar_rol_visor(email)
	else:
		if not frappe.db.exists("Has Role", {'parent': email, 'role': 'Visor de Puntuaciones'}):
			asignar_rol_visor(email)

	#Comprobamos si ya ha conseguido la carta
	if not frappe.db.exists("Incentivos", {"username": username, "project": project, "card": card}):
		incentivo = frappe.new_doc('Incentivos')
		incentivo.username = username
		incentivo.project = project
		incentivo.card = card
		incentivo.save(ignore_permissions=True)

	#Comprobamos si el usuario tiene ya creada las puntuaciones, y en caso contrario las creamos
	if not frappe.db.exists("Puntuaciones", username):
		puntuaciones = frappe.new_doc('Puntuaciones')
		puntuaciones.tailor_user = username
		puntuaciones.user = email
		puntuaciones.save(ignore_permissions=True)
		actualiza_tabla_cartas(username, puntuaciones)
		frappe.db.commit()
	else:
		puntuaciones = frappe.get_doc("Puntuaciones", username)
		actualiza_tabla_cartas(username, puntuaciones)
		puntuaciones.save(ignore_permissions=True)
		frappe.db.commit()
		return puntuaciones


def actualiza_tabla_cartas(username, puntuaciones):
	puntuaciones.cards = []
	puntuaciones.points = 0
	#incentivos = frappe.get_list("Incentivos",filters={"username": username},order_by="card")
	incentivos = frappe.db.sql("""select ti.card , tc.points as points from 
			`tabIncentivos` ti
			inner join `tabCarta` tc on ti.card = tc.name
			where username = %s
			order by ti.card
		""", (username), as_dict=True)

	for incentivo in incentivos:
		carta = frappe._dict({
		    'card_name': incentivo.card
		})
		puntuaciones.append("cards", carta)
		puntuaciones.points += incentivo.points

def actualiza_puntuaciones_en_masivo():
	usuarios = frappe.db.sql(""" select distinct(username) from `tabIncentivos`	""", as_dict=True)

	for usuario in usuarios:
		if not frappe.db.exists("Puntuaciones", usuario.username):
			puntuaciones = frappe.new_doc('Puntuaciones')
			puntuaciones.tailor_user = usuario.username
			puntuaciones.user = usuario.username
			puntuaciones.save(ignore_permissions=True)
			actualiza_tabla_cartas(usuario.username, puntuaciones)
		else:
			puntuaciones = frappe.get_doc("Puntuaciones", usuario.username)
			actualiza_tabla_cartas(usuario.username, puntuaciones)
			puntuaciones.save(ignore_permissions=True)
			frappe.db.commit()

def asignar_rol_visor(email):
	role = frappe.new_doc('Has Role')
	role.role = "Visor de Puntuaciones"
	role.parent = email
	role.parentfield = "roles"
	role.parenttype = "User"
	role.save(ignore_permissions=True)

@frappe.whitelist(allow_guest = True)
def trazar_error(mensaje):
	#frappe.db.sql('insert into `errores`(`error`) values (%(mensaje)s)',{'mensaje':mensaje})
	#frappe.db.commit()
	return "pongggeee"