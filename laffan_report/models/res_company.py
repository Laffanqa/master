from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    beneficiary_name = fields.Char(string="Beneficiary Name")
    iban = fields.Char(string="IBAN")
    swift_code = fields.Char(string="Swift Code")
    branch_address = fields.Char(string="Branch Address")
    account_type = fields.Char(string="Account Type")
    currency_id = fields.Many2one('res.currency', string='Currency')
    bank_name = fields.Char(string="Bank Name")
