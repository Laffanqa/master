# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesReport(models.Model):
    _inherit = 'sale.order'

    account_manager = fields.Many2one('res.users', string="Accounts Manager")
    project_id = fields.Many2one('project.project')


class AccountMove(models.Model):
    _inherit = 'account.move'

    account_manager = fields.Many2one('res.users', string="Accounts Manager")
    project_id = fields.Many2one('project.project')
    cust_ref = fields.Char(string="Reference")
