import frappe
from erpnext import get_default_company
from frappe.utils import get_system_timezone


@frappe.whitelist()
def get_settings():
	settings_doc = frappe.get_cached_doc("Sales Portal Settings", None)

	out = frappe._dict({
		"company": settings_doc.company or get_default_company(),
		"hide_items_without_image": settings_doc.hide_items_without_image,
		"show_customer_description": settings_doc.show_customer_description,

		# Formatting settings
		"number_format": frappe.get_system_settings("number_format"),
		"rounding_method": frappe.get_system_settings("rounding_method"),
		"date_format": frappe.get_system_settings("date_format"),
		"float_precision": frappe.get_system_settings("float_precision"),
		"currency_precision": frappe.get_system_settings("currency_precision"),
		"first_day_of_the_week": frappe.get_system_settings("first_day_of_the_week"),
		"system_timezone": get_system_timezone(),
		"user_timezone": frappe.db.get_value("User", frappe.session.user, "time_zone"),
	})

	return out
