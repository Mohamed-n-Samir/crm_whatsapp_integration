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
    
