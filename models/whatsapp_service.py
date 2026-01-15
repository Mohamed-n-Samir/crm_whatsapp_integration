from odoo import models, api



class WhatsAppService(models.AbstractModel):
    
    _name = 'whatsapp.service'
    _description = 'WhatsApp API Service'
    
    
    # Helper Methods
    def _correct_phone_number_structure(self):
        pass
    
    def _check_connection(self):
        pass