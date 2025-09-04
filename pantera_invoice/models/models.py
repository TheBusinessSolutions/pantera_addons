# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    total_refund_amount = fields.Float(string='Total refund',compute='compute_total_refund_amount')

    @api.depends('refund_invoice_ids')
    def compute_total_refund_amount(self):
        for rec in self:
            rec.total_refund_amount = 0.0
            if rec.refund_invoice_ids:
                rec.total_refund_amount = sum(rec.refund_invoice_ids.mapped('amount_total'))

