# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesReport(models.Model):
    _inherit = 'sale.order'

    account_manager = fields.Many2one('res.users', string="Accounts Manager")