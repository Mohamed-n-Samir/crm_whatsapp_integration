{
    "name": "CRM Whatsapp Integration",
    "version": "19.0.1.0.0",
    "category": "Sales/CRM",
    "author": "Mohamed Samir",
    "description": """This module integrates WhatsApp messaging capabilities into the CRM module,
                        allowing salespeople to send WhatsApp messages to leads/opportunities with
                        a single click for Odoo 19.""",
    "license": 'LGPL-3',
    "depends": ["crm"],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    "assets": {
    },
    "application": False,
    "installable": True,
}
