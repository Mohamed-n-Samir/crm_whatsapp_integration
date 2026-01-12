from odoo import fields, models, api



class CrmLead(models.Model):
    
    _inherit = 'crm.lead'
    
    whatsapp_phone = fields.Char(string='WhatsApp Number', compute='_compute_whatsapp_phone')
    
    
    
    # Compute Methods
    def _compute_whatsapp_phone(self):
        pass