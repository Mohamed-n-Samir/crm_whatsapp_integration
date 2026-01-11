from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    whatsapp_provider = fields.Selection(
        [("meta", "Meta Cloud API")],  # One for now
        string="Whatsapp Provider",
        default="meta",
        help="Select the WhatsApp API provier to use.",
    )

    whatsapp_default_template = fields.Text(
        string="Default Message Template",
        default="""Hello 'contact', thanks for your interest in our company 
                    we will contact you shortly. - 'salesperson'""",
        help="default message template for whatsapp messages",
    )

    whatsapp_meta_access_token = fields.Char(
        string="Meta Access Token", help="Your Meta WhatsApp Business API access token."
    )
    whatsapp_meta_phone_number_id = fields.Char(
        string="Meta Phone Number ID",
        help="your WhatsApp Business Phone Number ID from Meta",
    )
