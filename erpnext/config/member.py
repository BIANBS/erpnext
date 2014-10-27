from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Database of members."),
				},
                                {
                                        "type": "doctype",
                                        "name": "Contact",
                                        "description": _("All Contacts."),
                                },
                                {
                                        "type": "doctype",
                                        "name": "Address",
                                        "description": _("All Addresses."),
                                },
			]
		}
	]
