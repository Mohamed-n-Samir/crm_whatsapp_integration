from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    whatsapp_provider = fields.Selection(
        [("meta", "Meta Cloud API")],  # One for now
        string="Whatsapp Provider",
        default="meta",
        config_parameter="whatsapp.provider",
        help="Select the WhatsApp API provier to use.",
    )

    # whatsapp_default_template = fields.Text(
    #     string="Default Message Template",
    #     default="""Hello 'contact', thanks for your interest in our company 
    #                 we will contact you shortly. - 'salesperson'""",
    #     config_parameter="whatsapp.default_template",
    #     help="default message template for whatsapp messages",
    # )

    whatsapp_meta_access_token = fields.Char(
        string="Meta Access Token",
        help="Your Meta WhatsApp Business API access token.",
        config_parameter="whatsapp.meta_access_token",
    )
    whatsapp_meta_phone_number_id = fields.Char(
        string="Meta Phone Number ID",
        help="your WhatsApp Business Phone Number ID from Meta",
        config_parameter="whatsapp.meta_phone_number_id",
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
