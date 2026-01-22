from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    whatsapp_provider = fields.Selection(
        related='company_id.whatsapp_provider',
        readonly=False,
        help="Select the WhatsApp API provier to use.",
    )

    whatsapp_message_template = fields.Many2one(
        related='company_id.whatsapp_message_template',
        readonly=False,
        help="message template for whatsapp messages",
    )

    whatsapp_meta_access_token = fields.Char(
        related="company_id.whatsapp_meta_access_token",
        help="Your Meta WhatsApp Business API access token.",
        readonly=False,
    )
    whatsapp_meta_phone_number_id = fields.Char(
        related='company_id.whatsapp_meta_phone_number_id',
        help="your WhatsApp Business Phone Number ID from Meta",
        readonly=False,
    )

    whatsapp_api_is_configured = fields.Boolean(
        string="WhatsApp Configured",
        compute="_compute_whatsapp_api_is_configured",
    )

    # Methods
    def _compute_whatsapp_api_is_configured(self):

        for record in self:
            if record.whatsapp_provider == "meta":
                record.whatsapp_api_is_configured = bool(
                    record.whatsapp_meta_access_token
                    and record.whatsapp_meta_phone_number_id
                )

            else:
                record.whatsapp_api_is_configured = False

    # Actions
    def action_test_api_connection(self):

        message = "Configuration is correct."
        title = "Configuration is correct."
        notification_type = "success"

        if not self.whatsapp_api_is_configured:
            message = "Please fill in all required fields for your selected provider."
            title = "Configuration Incomplete"
            notification_type = "warning"

        return {
            "type": "ir.actions.client",
            "tag": "display_notification",
            "params": {
                "title": title,
                "message": message,
                "type": notification_type,
                "sticky": False,
            },
        }
        