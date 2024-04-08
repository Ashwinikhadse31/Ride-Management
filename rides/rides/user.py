import frappe
from frappe import _

def validate_last_name(doc,methods):
    if not doc.last_name:
        frappe.throw(_("Last Name is Mandatory"))
