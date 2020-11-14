# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "alerta_alcohol"
app_title = "Alerta Alcohol"
app_publisher = "Pedro Antonio Fernandez Gomez"
app_description = "Alerta Alcohol"
app_icon = "octicon octicon-report"
app_color = "#B83A3C"
app_email = "pedro@hispalisdigital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/alerta_alcohol/css/alerta_alcohol.css"
# app_include_js = "/assets/alerta_alcohol/js/alerta_alcohol.js"

# include js, css files in header of web template
# web_include_css = "/assets/alerta_alcohol/css/alerta_alcohol.css"
# web_include_js = "/assets/alerta_alcohol/js/alerta_alcohol.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
website_user_home_page = "/puntuaciones"

# Website user home page (by function)
# get_website_user_home_page = "alerta_alcohol.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "alerta_alcohol.install.before_install"
# after_install = "alerta_alcohol.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alerta_alcohol.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"alerta_alcohol.tasks.all"
# 	],
# 	"daily": [
# 		"alerta_alcohol.tasks.daily"
# 	],
# 	"hourly": [
# 		"alerta_alcohol.tasks.hourly"
# 	],
# 	"weekly": [
# 		"alerta_alcohol.tasks.weekly"
# 	]
# 	"monthly": [
# 		"alerta_alcohol.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "alerta_alcohol.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "alerta_alcohol.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "alerta_alcohol.task.get_dashboard_data"
# }

