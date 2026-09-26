# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    total_refund_amount = fields.Float(string='Total refund', compute='compute_total_refund_amount')

    @api.depends('refund_invoice_ids')
    def compute_total_refund_amount(self):
        for rec in self:
            rec.total_refund_amount = 0.0
            if rec.refund_invoice_ids:
                rec.total_refund_amount = sum(rec.refund_invoice_ids.mapped('amount_total'))

    def print_pantera_inv_with_stamp(self):
        """Trigger the specific report action for invoice with stamp"""
        return self.env.ref('pantera_invoice.action_report_inv_pantera_with_stamp').report_action(self)
# # -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class AccountMove(models.Model):
#     _inherit = 'account.move'

#     total_refund_amount = fields.Float(string='Total refund',compute='compute_total_refund_amount')

#     @api.depends('refund_invoice_ids')
#     def compute_total_refund_amount(self):
#         for rec in self:
#             rec.total_refund_amount = 0.0
#             if rec.refund_invoice_ids:
#                 rec.total_refund_amount = sum(rec.refund_invoice_ids.mapped('amount_total'))

