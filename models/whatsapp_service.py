from odoo import models, api
from odoo.exceptions import ValidationError

import re


class WhatsAppService(models.AbstractModel):

    _name = "whatsapp.service"
    _description = "WhatsApp API Service"

    # Helper Methods
    def _get_coutry_calling_code(self, country_code):

        if not country_code:
            return None

        country = self.env["res.country"].search(
            [("code", "=", country_code.upper())], limit=1
        )

        return country.phone_code if country else None


    # Configuration Helpers
    def _get_config(self, key, default=None):
        return self.env['ir.config_parameter'].sudo().get_param(key, default)
    
    def _get_provider(self):
        return self._get_config('whatsapp.provider', 'meta')
    
    def _is_configured(self):
        
        provider = self._get_provider()
        
        if provider == 'meta':
            token = self._get_config('whatsapp.meta_access_token')
            phone_id = self._get_config('whatsapp.meta_phone_number_id')
            return bool(token and phone_id)
        # elif: one for now
        
        return False
    
    def message_default_template(self):
        return self._get_config('whatsapp.default_template', "hello 'contact_name', thanks for your interest in 'company'. we will contact you shortly. - 'salesperson'")

    # Methods
    def normalize_phone_e164(self, phone, country=None):

        if not phone:
            raise ValidationError("Phone Number is required!")

        digits = re.sub(r"[^\d]", "", phone)

        if phone.strip().startswith("+"):
            return "+" + digits

        if not country or not country.phone_code:
            raise ValidationError("Country is required to normalize phone number")
        
        if digits.startswith('0'):
            digits = digits[1:]
            
        normalized = f"+{country.phone_code}{digits}"
        
        if not (7 <= len(re.sub(r'[^\d]', '', normalized)) <= 15):
            raise ValidationError("Invalid phone number")
        
        return normalized

    def send_message(self):
        pass
    
