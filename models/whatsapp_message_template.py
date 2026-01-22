from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class WhatsAppMessageTemplate(models.Model):
    
    _name = 'whatsapp.message.template'
    _description = 'WhatsApp Message Template'

    name = fields.Char(string='Template Name', required=True, index=True)
    body = fields.Text(string='Message Body', required=True,
                       help="Message body. You can include placeholders like {contact_name}, {company}.")
    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company,
        help="If set, this template is owned by the selected company. If empty, template is global.")
    active = fields.Boolean(default=True)

    @api.constrains('name', 'company_id')
    def _check_unique_name_per_company(self):

        for rec in self:
            domain = [('name', '=', rec.name)]
            if rec.company_id:
                domain.append(('company_id', '=', rec.company_id.id))
            else:
                domain.append(('company_id', '=', False))
            others = self.search(domain)
            if len(others) > 1:
                raise ValidationError(_("A template with this name already exists for the same company."))
