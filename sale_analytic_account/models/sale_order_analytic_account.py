# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleOrderanalyticAccount(models.Model):
    _inherit = "sale.order"


    def _action_confirm(self):
        """ On SO confirmation, analytic account will be created automatically. """
        result = super(SaleOrderanalyticAccount, self)._action_confirm()
        # if the SO not already linked to analytic account, create a new analytic account and set to so analytic account.
        for order in self:
            if not order.analytic_account_id:
                order._create_analytic_account()
        return result

