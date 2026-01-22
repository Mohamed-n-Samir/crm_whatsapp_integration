from odoo import fields, models


class ResCompany(models.Model):
    
    _inherit = 'res.company'
    
    whatsapp_provider = fields.Selection(
        [("meta", "Meta Cloud API")],  # One for now
        string="Whatsapp Provider",
        help="Select the WhatsApp API provier to use.",
    )

    whatsapp_meta_access_token = fields.Char(
        string="Meta Access Token",
        help="Your Meta WhatsApp Business API access token.",
    )
    
    whatsapp_meta_phone_number_id = fields.Char(
        string="Meta Phone Number ID",
        help="your WhatsApp Business Phone Number ID from Meta",
    )
    
    whatsapp_message_template = fields.Many2one(
        comodel_name='whatsapp.message.template',
        help="message template for whatsapp messages",
        ondelete='set null',
        domain="['|', ('company_id', '=', False), ('company_id', '=', id)]"
    )