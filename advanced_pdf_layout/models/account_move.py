from odoo import models, fields, api
import calendar
import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'

    payment_type = fields.Selection([('cash', 'Cash'), ('cheque', 'Cheque'), ('credit_card', 'Credit Card')],
                                    string="Payment Type", default='cash')
    first_date = fields.Date(compute='compute_invoice_date')
    last_date = fields.Date(compute='compute_invoice_date')

    @api.depends('invoice_date')
    def compute_invoice_date(self):
        first_date =''
        last_date =''
        for rec in self:
            if rec.invoice_date:
                month = rec.invoice_date.month
                year = rec.invoice_date.year
                first, last = calendar.monthrange(year, month)
                datetime.datetime(year, month, 1)
                first_date = datetime.datetime(year, month, 1)
                last_date = datetime.datetime(year, month, last)
            rec.first_date = first_date
            rec.last_date = last_date

