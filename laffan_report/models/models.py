# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SalesReport(models.Model):
    _inherit = 'sale.order'

    account_manager = fields.Many2one('res.users', string="Accounts Manager")
    project_id = fields.Many2one('project.project', string="Project")

    def action_view_invoice(self):
        res = super(SalesReport, self).action_view_invoice()
        if res:
            if res.get('account_manager', False):
                res['account_manager'] = self.account_manager.id
            if res.get('project_id', False):
                res['project_id'] = self.project_id.id
        print("resssssssss", res)
        return res

    # def _create_invoices(self, grouped=False, final=False, date=None):
    #     print("fddddddddd")
    #     res = super(SalesReport, self)._create_invoices(grouped, final, date)
    #     if res['account_manager']:
    #         res['account_manager'] = self.account_manager.id
    #     if res['project_id']:
    #         res['project_id'] = self.project_id.id
    #     print("resssssssss",res)
    #     return res


class AccountMove(models.Model):
    _inherit = 'account.move'

    account_manager = fields.Many2one('res.users', string="Accounts Manager")
    project_id = fields.Many2one('project.project')
    cust_ref = fields.Char(string="Reference")
